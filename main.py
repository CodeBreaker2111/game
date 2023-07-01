import sys
import pygame; pygame.init()
import json

import assets as assets
import window as window
import blocks as blocks
import enemy_spawn as enemy_spawn

skinNum = 1
skin = assets.player_skin1
sprinting = False
enemy_spawn.spawn_enemy((100, 100), 1)
player_save_posx = assets.player_save_posx
player_save_posy = assets.player_save_posy

def key_pressed():
    return pygame.key.get_pressed()

def stamina(pressed):
    global sprinting

    if pressed:
        sprinting = True
    
    if pressed == False:
        sprinting = False

def main():
    global skin
    global skinNum
    global sprinting
    global player_save_posx
    global player_save_posy

    keyW_pressed = False
    keyA_pressed = False
    keyS_pressed = False
    keyD_pressed = False

    clock = pygame.time.Clock()

    while True:
        clock.tick(assets.fps)
        # detect closing window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                json_data = None
                blocks.save()
                with open("assets/json/player.json", "r") as f:
                    data = f.read()
                    json_data = json.loads(data)
                with open("assets/json/player.json", "w") as f:
                    json_data["posx"] = player_save_posx
                    json_data["posy"] = player_save_posy

                    json.dump(json_data, f, indent=1)
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    keyW_pressed = True
                if event.key == pygame.K_a:
                    keyA_pressed = True
                if event.key == pygame.K_s:
                    keyS_pressed = True
                if event.key == pygame.K_d:
                    keyD_pressed = True

                if event.key == pygame.K_LSHIFT:
                    if assets.player.stamina > 50:
                        stamina(True)
                
                if event.key == pygame.K_k:
                    if skinNum == 1:
                        skinNum = 2
                    elif skinNum == 2:
                        skinNum = 1
                
                if event.key == pygame.K_p:
                    player_save_posx = assets.player.pos[0]
                    player_save_posy = assets.player.pos[1]
                        
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    keyW_pressed = False
                if event.key == pygame.K_a:
                    keyA_pressed = False
                if event.key == pygame.K_s:
                    keyS_pressed = False
                if event.key == pygame.K_d:
                    keyD_pressed = False

                if event.key == pygame.K_LSHIFT:
                    stamina(False)
            
        if keyW_pressed:
            assets.player.move(0, -assets.player_speed)
        if keyA_pressed:
            assets.player.move(-assets.player_speed, 0)
        if keyS_pressed:
            assets.player.move(0, assets.player_speed)
        if keyD_pressed:
            assets.player.move(assets.player_speed, 0)

        window.fill((150, 150, 200))

        blocks.main()

        # list item 0 = skin, list item 1 = position
        window.blit(assets.red_cross, (player_save_posx + 40, player_save_posy + 70))
        enemy_spawn.draw()
        window.blit(assets.player.skin, assets.player.pos)
        enemy_spawn.move_to(assets.player.pos)

        if assets.player.last_stamina != assets.player.stamina:
            stamina_gradient_data = window.crop(assets.stamina_gradient_png, (0, 0, assets.player.stamina, 20))
            window.blit(pygame.transform.scale(pygame.image.load(stamina_gradient_data), (assets.player.stamina * 2, 40)), (82, 924))
        else:
            window.blit(pygame.transform.scale(pygame.image.load(assets.stamina_gradient_png), (assets.player.stamina * 2, 40)), (82, 924))
        window.blit(pygame.transform.scale(assets.stamina_bar, (340, 140)), (60, 840))

        window.update()

        if skinNum == 1 and skin == assets.player_skin2:
            skin = assets.player_skin1
            assets.player.skin = skin
        if skinNum == 2 and skin == assets.player_skin1:
            skin = assets.player_skin2
            assets.player.skin = skin
        
        # Stamina / sprinting stuff
        if assets.player.stamina < 1:
            stamina(False)
        if sprinting:
            assets.player_speed = 1.75
            assets.player.sprint_stamina()
        else:
            assets.player_speed = 0.8
            if assets.player.stamina < 150:
                assets.player.recharge_stamina()
            if assets.player.stamina > 150:
                assets.player.stamina = 150
main()
