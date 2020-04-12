import math
from data.data_controller import DataController

class SimulationController:
    def conductSimulationLogic(self, sim_objects):

            # for the time being, assume all sim_objects are balls. change later! TODO
        for i in range(len(sim_objects)-1):
            j = i + 1
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
                    
                    
                    # TODO take into account recovery


                j += 1


