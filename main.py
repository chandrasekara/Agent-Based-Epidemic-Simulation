import pygame
from pygame.locals import *
from random import random

from sim_objects.point import Point

pygame.init()

display_width = 640
display_height = 480

# colour defs, should be in it's own class/file

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('COVID-19 Simulation')
clock = pygame.time.Clock()

circleImg = pygame.image.load('static/ball.png')


point_objs = []

for i in range(20):
    point_objs.append(Point(random(),random()))


for point in point_objs:
    print("Point obj with x: " + str(point.x) + " and y: " + str(point.y))



def display_circle(x,y):
    gameDisplay.blit(circleImg, (x,y))

running = 1

# really should be using obj oriented for this sort of stuff lol

circ_x = 300
circ_y = 300

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0
    else:
      #print event
      pass
          
  gameDisplay.fill(white)
  display_circle(circ_x, circ_y)
  pygame.display.update()
  clock.tick(60)


pygame.quit()
