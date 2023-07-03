import pygame; pygame.init()
import window as window
import assets as assets

def draw():
    for enemy in assets.enemy_list:
        list_index = 0
        window.blit(assets.enemy1, (assets.enemy_list[list_index][0], assets.enemy_list[list_index][1]))
        list_index += 1

def spawn_enemy(pos, type):
    assets.enemy_list.append((pos[0], pos[1], type))

def move_to(point):
    for enemy in assets.enemy_list:
        list_index = 0
        X = assets.enemy_list[list_index][0]
        Y = assets.enemy_list[list_index][1]
        x = 0
        y = 0
        axv = 0
        ayv = 0
        ax = False
        ay = False
        if X < point[0]:
            x = X + 0.15
            axv = 0
            if (assets.player.pos[0] - x) < 50:
                ax = True
        if X > point[0]:
            x = X - 0.15
            axv = 1
            if (x - assets.player.pos[0]) < 50:
                ax = True
        if Y < point[1]:
            y = Y + 0.15
            ayv = 0
            if (assets.player.pos[1] - y) < 50:
                ay = True
        if Y > point[1]:
            y = Y - 0.15
            ayv = 0
            if (y - assets.player.pos[1]) < 50:
                ay = True

        if ax and ay:
            assets.player.damage(0.03)

        assets.enemy_list[list_index] = (x, y, 1)
        list_index += 1
