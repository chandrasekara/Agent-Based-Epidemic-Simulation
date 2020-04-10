from random import random
from simulation_object import SimulationObject
import math

MAX_RADIANS = 2 * math.pi

MAX_VELOCITY = 10

class Point(SimulationObject):

    def __init__(self, imageFile, x_in, y_in, specified_velocity=None):
        SimulationObject.__init__(imageFile, x_in, y_in)
        if specified_velocity == None:
            self.velocity = (random()*MAX_DEGREES, MAX_VELOCITY/2)

    def update():
        SimulationObject.__init__()
        direction = velocity[0]
        speed = velocity[1]
        self.x += math.cos(direction) * speed
        self.y += math.sin(direction) * speed


    def thing(self):
        pass


