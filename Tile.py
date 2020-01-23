from Setup import *



class Tile:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.radius = 60
    def draw(self):
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), self.radius, 2)
        pygame.display.update()
    def inside(self, pos):
        X = pos[0]
        Y = pos[1]
        dist = round(math.sqrt(((X - self.x) ** 2) + ((Y - self.y) ** 2)))
        if dist < self.radius:
            return True
        else:
            return False








