
# Author: Shaik Faizan Roshan Ali
# Date: 12th August 2021
# About : Finding the convex hull of points in an catesian 2-Dimesnional Plane
# Current State: Bug in counter-clock wise selection in findConvexHull

import random 
import sys
from math import atan
import matplotlib.pyplot as plt

def crossProduct(point1, point2, point3):

    vector1 = ((point2[0] - point1[0]), (point2[1] - point1[1])) 
    vector2 = ((point3[0] - point1[0]), (point3[1] - point1[1]))

    # (x1 * y2) - (x2 * y1) cross product formula
    value = (vector1[0] * vector2[1]) - ( vector2[0] * vector1[1]) 

    return value

def getSlope(point1, point2):

    # (y2 - y1) / (x2 - x1)
    if(point1[0] == point2[0]): # when both x coordinates are same tangent value is infinity

        return sys.maxsize
    else:
        
        slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
        return atan(slope)

def findConvexHull(points):

    stack = []
    points.sort() # find the point with least (x, y) coordinates
    print(points)
    stack.append(points.pop(0)) # pop and push the least element into the stack

    # Now, For traversing counter-clock wise
    # We need to sort it by the following priority order
    # slope, least y value, 
    points.sort(key=lambda point: (getSlope(stack[0], point), -point[1], point[0]))
    # print(stack[0], points) # for checking the first selection point

    # append the least slope point into the stack.
    stack.append(points.pop(0))
   
    for index in range(0, len(points)):

        crossProd = crossProduct(stack[-2], stack[-1], points[index])
        if(crossProd < 0):

            stack.pop()
            stack.append(points[index])
        else:

            stack.append(points[index])
    
    return stack

def plotGraph(points):

    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y)
    for index in range(0, len(x)):

        plt.text(x[index], y[index], str((x[index], y[index])))
    plt.show()

if __name__ == '__main__':

    # points = [(random.randint(0, 10), random.randint(0, 10)) for i in range(10)] # taking random points
    points = [(0, 8), (1, 3), (3, 9), (5, 4), (6, 10), (8, 1), (8, 9), (9, 0), (10, 1), (10, 3)]
    
    coordinates = points.copy()
    
    hull = findConvexHull(points)
    print("hull: ", hull)
    plotGraph(coordinates) # to visualise the coordinates
