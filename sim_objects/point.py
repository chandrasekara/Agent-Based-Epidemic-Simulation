from random import random

class Point:

    def __init__(self, x_in, y_in):
        self.x = x_in
        self.y = y_in


point_objs = []

for i in range(20):
    point_objs.append(Point(random(),random()))


for point in point_objs:
    print("Point obj with x: " + str(point.x) + " and y: " + str(point.y))

