import pygame; pygame.init(); pygame.mixer.init()
import player as player_file
import json
import window as window

player_skin1 = pygame.transform.scale(pygame.image.load("assets/player/skin1.png"), (80, 140))
player_skin2 = pygame.transform.scale(pygame.image.load("assets/player/skin2.png"), (80, 140))

player_speed = 0.35

player = player_file.player(100, 100, 0, 0, player_skin1, (100, 100), 150, player_skin1.get_rect())
player.last_pos = player.pos

stamina_gradient_png = "assets/stamina_gradient.png"
stamina_bar = pygame.image.load("assets/stamina_bar.png")
stamina_bytesio = []

blocks = ["assets/blocks/wood.png", "assets/blocks/metal.png", "assets/transparent.png"]
blocks_rect = []
block_select = pygame.image.load("assets/blocks/block_select.png")

enemy1 = pygame.transform.scale(pygame.image.load("assets/enemy/soldier1.png"), (80, 140))
enemy_list = [(100, 100, 1)]

fps = 780

background = pygame.image.load("assets/background.png")

json_data = None
with open("assets/json/world.json", "r") as f:
    data = f.read()
    json_data = json.loads(data)

print(json_data)

with open("assets/json/world.josn", "w") as f:
    if len(json_data["blocks"]) < 5:
        pass
    else:
        for i in range(1, 800):
            json_data["blocks"].append(-1)
    
        json.dump(json_data, f, indent = 1)

for i in range(1, 150):
    stamina_bytesio.append(window.crop(stamina_gradient_png, (0, 0, i, 20)))

stamina_bytesio.append(window.crop(stamina_gradient_png, (0, 0, 150, 20)))
print(len(stamina_bytesio))