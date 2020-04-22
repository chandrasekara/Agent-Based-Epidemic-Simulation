from pygame.locals import *
from random import random
from sim_objects.point import Point
from sim_objects.util.game_info import *
from sim_objects.util.colors import *
from logic.sim_controller import SimulationController
from data.graph import *
import argparse

# set default parameters
DEFAULT_NUM_AGENTS = 80
DEFAULT_INITIAL_INFECTED = 3
DEFAULT_INFECTION_RECOVERY_PERIOD = 200
DEFAULT_SOCIAL_DISTANCING_FACTOR = 0

# pygame configuration parameters
TICK_PER_UPDATE = 60

# parse command line arguments
parser = argparse.ArgumentParser(description='Simulate the spread of an infectious virus')
parser.add_argument('-a', '--agents', type=int, help='Number of Agents')
parser.add_argument('-i', '--infected', type=int, help='Number of Initially Infected Agents')
parser.add_argument('-r', '--recovery', type=int, help='The number of ticks for an infected agent to recover')
parser.add_argument('-d', '--social-distancing', type=int, help='The percentage of agents that follow social' +
                                                               'distancing', dest="social_distancing_factor")
parser.add_argument('--default', help='use the default settings', action='store_true')
args = parser.parse_args()

# TODO: Implement for simulation end or delete
def message_to_screen(msg):
    font = pygame.font.SysFront(None, 400)
    screen_text = font.render(msg, True, (0, 0, 0))
    gameDisplay.blit(screen_text, [640/2, 480/2])


# TODO: Move these functions to a better place
def initialize_simulation_objects(number_of_agents, initial_infected, infection_recovery_period,
                                  social_distancing_factor):
    sim_objs = []
    for i in range(number_of_agents):
        sim_objs.append(
            Point(BALL_SPRITE, random() * DISPLAY_WIDTH, random() * DISPLAY_HEIGHT, infection_recovery_period,
                  social_distancing_factor))
    for i in range(initial_infected):
        sim_objs[i].infect()
    return sim_objs


if args.default:
    number_of_agents = DEFAULT_NUM_AGENTS
    initial_infected = DEFAULT_INITIAL_INFECTED
    infection_recovery_period = DEFAULT_INFECTION_RECOVERY_PERIOD
    social_distancing_factor = DEFAULT_SOCIAL_DISTANCING_FACTOR
    # TODO: Move to better global game information object
    sim_objs = initialize_simulation_objects(number_of_agents, initial_infected, infection_recovery_period,
                                             social_distancing_factor)
else:
    number_of_agents = args.agents
    initial_infected = args.infected
    infection_recovery_period = args.recovery
    social_distancing_factor = args.social_distancing_factor
    # TODO: Move to better global game information object
    try:
        sim_objs = initialize_simulation_objects(number_of_agents, initial_infected, infection_recovery_period,
            social_distancing_factor)
    except:
        parser.print_help()
        exit()

# initiate pygame and display
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
    gameDisplay.fill(white)
    infect_count = 0
    for point in sim_objs:
        if point.infected is True:
            infect_count += 1
        point.update()
        point.display(gameDisplay)
    if infect_count == 0:
        running = 0
    sim_controller.conductSimulationLogic(sim_objs)
    pygame.display.update()
    clock.tick(TICK_PER_UPDATE)

sim_controller.close()
pygame.quit()
display_results('results.csv')
