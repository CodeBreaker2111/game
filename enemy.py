class enemy:
    def __init__(self, skin, hat, x, y) -> None:
        self.skin = skin
        self.hat = hat

        self.pos = (x, y)
        self.posX = x
        self.posY = y
    
    def follow_point(self, point):
        # x position
        if self.pos[0] < point[0]:
            self.posX += 0.5
        elif self.pos[0] > point[0]:
            self.posX -= 0.5
        
        # y position
        if self.pos[1] < point[1]:
            self.posY += 0.5
        elif self.pos[1] > point[1]:
            self.posY -= 0.5
