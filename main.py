import pygame
from pygame.locals import *
from random import random
import time
from sim_objects.point import Point
from sim_objects.util.game_info import *
from sim_objects.util.colors import *
from logic.sim_controller import SimulationController
from data.graph import *
import argparse

DEFAULT_NUM_AGENTS = 80
DEFAULT_INITIAL_INFECTED = 3

parser = argparse.ArgumentParser(description='Simulate the spread of an infectious virus')
parser.add_argument('-a','--agents', type=int, help='Number of Agents')
parser.add_argument('-i', '--infected', type=int, help='Number of Initially Infected Agents')
parser.add_argument('--default', help='use the default settings', action='store_true')
args = parser.parse_args()

if args.default:

    number_of_agents = DEFAULT_NUM_AGENTS
    initial_infected = DEFAULT_INITIAL_INFECTED
    # TODO: Move to better global game information object

    sim_objs = []

    for i in range(number_of_agents):
        sim_objs.append(Point(BALL_SPRITE, random()*DISPLAY_WIDTH,random()*DISPLAY_HEIGHT))

    for i in range(initial_infected):
        sim_objs[i].infect()

else:
    

    number_of_agents = args.agents
    initial_infected = args.infected
    # TODO: Move to better global game information object

    sim_objs = []

    try:
        for i in range(number_of_agents):
            sim_objs.append(Point(BALL_SPRITE, random()*DISPLAY_WIDTH,random()*DISPLAY_HEIGHT))

        for i in range(initial_infected):
            sim_objs[i].infect()
    except:
        parser.print_help()
        exit()

pygame.init()

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Epidemic Simulation')
clock = pygame.time.Clock()

sim_controller = SimulationController()


running = 1

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0
    else:
      #print event
      pass
          
  gameDisplay.fill(white)
  for point in sim_objs:
      point.update()
      point.display(gameDisplay)
  sim_controller.conductSimulationLogic(sim_objs)
  pygame.display.update()
  clock.tick(60)

sim_controller.close()

display_results('results.csv')

pygame.quit()
