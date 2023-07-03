import pygame; pygame.init(); pygame.mixer.init()
import player as player_file
import json
import window as window

player_skin1 = pygame.transform.scale(pygame.image.load("assets/player/skin1.png"), (80, 140))
player_skin2 = pygame.transform.scale(pygame.image.load("assets/player/skin2.png"), (80, 140))

player_speed = 0.35

player_save_posx = None
player_save_posy = None

with open("assets/json/player.json", "r") as f:
    data = f.read()
    json_data = json.loads(data)

    player_save_posx = json_data["posx"]
    player_save_posy = json_data["posy"]

player = player_file.player(player_save_posx, player_save_posy, 0, 0, player_skin1, (None), 150, player_skin1.get_rect(), 100)
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

for i in range(1, 150):
    stamina_bytesio.append(window.crop(stamina_gradient_png, (0, 0, i, 20)))

stamina_bytesio.append(window.crop(stamina_gradient_png, (0, 0, 150, 20)))

red_cross = pygame.image.load("assets/red_cross.png")