import pygame
import json
import assets as assets
import window as window

pygame.init()
pygame.mixer.init()

blocks_list = []

def read():
    with open("assets/json/world.json", "r") as f:
        data = f.read()
        json_data = json.loads(data)

        return json_data

blocks_list = read()["blocks"]

def draw():
    global blocks_list

    posX = 0
    posY = 0

    for block in blocks_list:
        if posX >= 1950:
            posX = 0
            posY += 50
        if block != -1:
            window.blit(pygame.image.load(assets.blocks[block]), (posX, posY))
        posX += 50
            
def build_block():
    mbuttons_pressed = pygame.mouse.get_pressed()
    mposition = pygame.mouse.get_pos()
    tile_cornerx = 0
    tile_cornery = 0
    list_index = 0

    if mbuttons_pressed[0]:
        tile_cornerx = (mposition[0] // 50) * 50
        tile_cornery = (mposition[1] // 50) * 50
        
        list_index = int(tile_cornerx / 50 + ((tile_cornery / 50) * 39))

        json_data = None
        try:
            blocks_list[list_index] = 0
        except IndexError:
            print("you cant place here")
            pygame.mixer.music.load("assets/sound/cant_place.wav")
            pygame.mixer.music.play(0)
    
    if mbuttons_pressed[1]:
        tile_cornerx = (mposition[0] // 50) * 50
        tile_cornery = (mposition[1] // 50) * 50
        
        list_index = int(tile_cornerx / 50 + ((tile_cornery / 50) * 39))

        json_data = None
        try:
            blocks_list[list_index] = 1
        except IndexError:
            print("you cant place here")
            pygame.mixer.music.load("assets/sound/cant_place.wav")
            pygame.mixer.music.play(0)
    
    if mbuttons_pressed[2]:
        tile_cornerx = (mposition[0] // 50) * 50
        tile_cornery = (mposition[1] // 50) * 50
        
        list_index = int(tile_cornerx / 50 + ((tile_cornery / 50) * 39))

        json_data = None
        try:
            blocks_list[list_index] = -1
        except IndexError:
            print("you cant delete there")
            pygame.mixer.music.load("assets/sound/cant_delete.wav")
            pygame.mixer.music.play(0)

def block_select_icon():
    mposition = pygame.mouse.get_pos()

    tilecornerX = (mposition[0] // 50) * 50
    tilecornerY = (mposition[1] // 50) * 50

    window.blit(assets.block_select, (tilecornerX, tilecornerY))

def save():
    json_data = None
    with open("assets/json/world.json", "r") as f:
        data = f.read()
        json_data = json.loads(data)
    with open("assets/json/world.json", "w") as f:
        json_data["blocks"] = blocks_list
        json.dump(json_data, f, indent=1)

def main():
    global blocks_list
    build_block()
    draw()
    block_select_icon()
    save()
