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
