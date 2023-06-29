import pygame; pygame.init()
from PIL import Image
import io

# Define window
win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Game")

# Prety much just the blit function
def blit(image, pos):
    win.blit(image, pos)

# Prety much just the fill function
def fill(color):
    win.fill(color)

# Updates the screen
def update():
    pygame.display.update()

# Return a bytesio cropped image
def crop(image, crop):
    with Image.open(image) as im:
        data = io.BytesIO()
        cropped_image = im.crop(crop)
        cropped_image.save(data, "png")

        data.seek(0)

        return data