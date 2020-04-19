from random import random
from simulation_object import SimulationObject
import math
from util.game_info import *

MAX_VELOCITY = 2

class Point(SimulationObject):

    def __init__(self, imageFile, x_in, y_in, infection_recovery_period_in, social_distancing_factor_in,
                 specified_velocity=None):
        SimulationObject.__init__(self, imageFile, x_in, y_in)
        self.infected = False
        self.recovered = False
        self.infection_timer = 0
        self.infection_recovery_period = infection_recovery_period_in
        self.social_distancing_factor = social_distancing_factor_in
        if self.is_social_distancing():
            self.velocity = (0,0)
        else:
            if specified_velocity is None:
                speed_x = MAX_VELOCITY * random()
                self.velocity = (speed_x, math.sqrt(MAX_VELOCITY*MAX_VELOCITY - speed_x*speed_x))
            else:
                self.velocity = specified_velocity


    def is_social_distancing(self):
        if random() < float(self.social_distancing_factor)/100:
            return True
        else:
            return False

    def infect(self):
        self.image = BALL_INFECTED_SPRITE
        self.infected = True
    
    def update(self):
        SimulationObject.update(self)
        if self.x >= DISPLAY_WIDTH or self.x <= 0:
            self.bounce('x')
        if self.y >= DISPLAY_HEIGHT or self.y <= 0:
            self.bounce('y')
        dx = self.velocity[0]
        dy = self.velocity[1]
        self.y += dy
        self.x += dx

        if self.infected:
            self.infection_timer += 1
            if self.infection_timer > self.infection_recovery_period:
                self.recover()
    
    def recover(self):
        self.infected = False
        self.recovered = True
        self.image = BALL_RECOVERED_SPRITE
    

    def bounce(self, direction):
        if direction == 'x':
            self.velocity = (-self.velocity[0], self.velocity[1])
        else:
            self.velocity = (self.velocity[0], -self.velocity[1])
