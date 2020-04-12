class DataController:
    def __init__(self):
        self.clock = 0
        self.f = open('results.csv','w')
        self.f.write('Time,Infected\n')

    def tick(self, infected_number):
        self.clock += 1
        self.f.write(str(self.clock) + "," + str(infected_number) + "\n")

    def close(self):
        self.f.close()
