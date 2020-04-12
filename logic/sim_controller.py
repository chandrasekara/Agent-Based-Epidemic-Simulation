import math
from data.data_controller import DataController

class SimulationController:
    
    def __init__(self):
        self.data_controller = DataController()

    def conductSimulationLogic(self, sim_objects):
        num_infected = 0
        num_recovered = 0
        num_never_infected = 0
        # for the time being, assume all sim_objects are balls. change later! TODO
        for i in range(len(sim_objects)-1):
            j = i + 1
            if sim_objects[i].infected:
                num_infected += 1
            if sim_objects[i].recovered:
                num_recovered += 1
            if sim_objects[i].recovered == False and sim_objects[i].infected == False:
                num_never_infected += 1
            while j < len(sim_objects):
                xi = sim_objects[i].x
                xj = sim_objects[j].x
                yi = sim_objects[i].y
                yj = sim_objects[j].y

                if math.sqrt((xi-xj)**2 + (yi-yj)**2) < 16:
                    if (sim_objects[i].infected == False and sim_objects[j].infected == True):
                        sim_objects[i].infect()
                    if (sim_objects[i].infected == True and sim_objects[j].infected == False):
                        sim_objects[j].infect()    
                j += 1
        if sim_objects[-1].infected:
            num_infected += 1
        if sim_objects[-1].recovered:
            num_recovered += 1
        if sim_objects[-1].recovered == False and sim_objects[i].infected == False:
            num_never_infected += 1
        self.data_controller.tick(num_infected, num_recovered, num_never_infected)
    
    def close(self):
        self.data_controller.close()

