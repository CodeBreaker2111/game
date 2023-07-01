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
        if X < point[0]:
            x = X + 0.3 
        if X > point[0]:
            x = X - 0.3
        if Y < point[1]:
            y = Y + 0.3
        if Y > point[1]:
            y = Y - 0.3
        assets.enemy_list[list_index] = (x, y, 1)
        list_index += 1
