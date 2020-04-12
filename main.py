import pygame
from pygame.locals import *
from random import random
import time
from sim_objects.point import Point
from sim_objects.util.game_info import *
from sim_objects.util.colors import *

pygame.init()

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Epidemic Simulation')
clock = pygame.time.Clock()

point_objs = []

for i in range(10):
    point_objs.append(Point(BALL_SPRITE, random()*DISPLAY_WIDTH,random()*DISPLAY_HEIGHT))

running = 1

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0
    else:
      #print event
      pass
          
  gameDisplay.fill(white)
  for point in point_objs:
      point.update()
      point.display(gameDisplay)
  pygame.display.update()
  clock.tick(60)

pygame.quit()
