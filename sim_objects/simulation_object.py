import pygame

class SimulationObject:

    def __init__(self, imageFile, x_in, y_in):
        self.image = pygame.image.load(imageFile)
        self.x = x_in
        self.y = y_in

    def display(self, gameDisplay):
        gameDisplay.blit(self.image, (self.x, self.y))

    def update(self):
        pass
