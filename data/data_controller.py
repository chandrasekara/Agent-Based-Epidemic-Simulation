class DataController:
    def __init__(self):
        self.clock = 0
        self.f = open('results.csv','w')
        self.f.write('Time,Infected,Recovered,Never Infected\n')

    def tick(self, infected_number, recovered_number, never_infected_number):
        # record simulation result for one unit of time
        self.clock += 1
        self.f.write(str(self.clock) + "," + str(infected_number) + "," + str(recovered_number) + "," + str(never_infected_number) + "\n")

    def close(self):
        self.f.close()
