import pygame; pygame.init()

class player:
    def __init__(self, x, y, velX, velY, texture, size, stamina, rect) -> None:
        self.vel = (velX, velY)
        self.pos = (x, y)

        self.skin = texture
        self.size = size

        self.rect = rect

        self.stamina = stamina
        self.last_stamina = stamina

        self.last_move = None
    
    def move(self, speedX, speedY):
        self.pos = (speedX + self.pos[0], speedY + self.pos[1])

    def sprint_stamina(self):
        self.last_stamina = self.stamina
        self.stamina -= 0.2
        if self.stamina == 150:
            self.last_stamina = 150
    
    def recharge_stamina(self):
        self.last_stamina = self.stamina
        self.stamina += 0.1
        if self.stamina == 150:
            self.last_stamina = 150