
# Author: Shaik Faizan Roshan Ali
# Date: 18th August 2021
# About : Finding the convex hull of points in a cartesian 2-Dimensional Plane

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
    if(point1[0] == point2[0]): # when both x coordinates have same tangent value is infinity

        return sys.maxsize
    else:
        
        slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
        # print(atan(slope)) # for printing slope for analysis
        return atan(slope)

def findConvexHull(points):

    stack = [] # To store the hull
    points.sort() # find the point with least (x, y) coordinates
    print(points)
    stack.append(points.pop(0)) # pop and push the least element into the stack

    # Now, For traversing counter-clock wise
    # We need to sort points by the following priority order
    # slope, least y value, x values
    points.sort(key=lambda point: (getSlope(stack[0], point), -point[1], point[0]))
    # print(stack[0], points) # test analysis only

    # append the least slope point into the stack connecting the first 2 points.
    stack.append(points.pop(0))
   
    for index in range(0, len(points)):

        crossProd = crossProduct(stack[-2], stack[-1], points[index])
        if(crossProd < 0):

            stack.pop()
            stack.append(points[index])
        else:

            stack.append(points[index])

        # print("Stack at interation ", index, ": ", stack) # test analysis only
    
    return stack

# the plotGraph function is used for visualisation of the given coordinates.
def plotGraph(points):

    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y)

    # labeling coordinate values using plt.text method.
    for index in range(0, len(x)):

        plt.text(x[index], y[index], str((x[index], y[index])))
    plt.show()

if __name__ == '__main__':

    points = [(3, 4), (3, 10), (5, 8), (5, 9), (6, 3), (7, 4), (7, 10), (8, 1), (8, 1), (9, 7)]
    coordinates = points.copy() # for plotting
    hull = findConvexHull(points)
    print("hull coordinates: ", hull)
    plotGraph(coordinates)
