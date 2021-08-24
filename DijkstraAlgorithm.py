# Author : Shaik Faizan Roshan Ali
# Email : alsahercoder@gmail.com
# Date : 24th August 2021
# About : Implementation of Dijkstra's algorithm
import sys
class Graph:

    def __init__(self, vertices, graph):
        
        self.vertices = vertices
        self.graph = graph 
        self.path = []
        self.cost = []
        self.visited = [False for _ in range(vertices)]
    
    def findMinEdge(self, adjList):

        minimum = sys.maxsize
        minIndex = 0
        
        for index in range(0, self.vertices):

            if(adjList[index] < minimum 
                    and adjList[index] != 0 and self.visited[index] != True):

                minimum = adjList[index]
                minIndex = index
                
        return minIndex

    def dijkstra(self, source):

        current = source
        
        # append the source and path 
        self.path.append(source)
        self.cost.append(0)
        self.visited[source] = True

        for index in range(0, self.vertices-1):

            minimumEdge = self.findMinEdge(self.graph[current])

            # append the edge to the path and its respective cost
            self.path.append(minimumEdge)
            self.cost.append(self.cost[-1] + self.graph[current][minimumEdge])
            
            # update the visited array
            current = minimumEdge
            self.visited[minimumEdge] = True

        print("Path: ", self.path)
        print("Cost: ", self.cost)


if __name__ == "__main__":

    vertices = 8
    adjList = { 0 : [0, 0, 0, 0, 0, 0, 0, 0, 0],
                1 : [300, 0, 0, 0, 0, 0, 0, 0, 0],
                2 : [1000, 800, 0, 0, 0, 0, 0, 0, 0],
                3 : [0, 0, 1200, 0, 0, 0, 0, 0, 0],
                4 : [0, 0, 0, 1500, 0, 250, 0, 0, 0],
                5 : [0, 0, 0, 1000, 0, 0, 0, 900, 1400],
                6 : [0, 0, 0, 0, 0, 0, 0, 0, 1000],
                7 : [1700, 0, 0, 0, 0, 0, 0, 0, 0],
            }
    graph = Graph(vertices, adjList)
    graph.dijkstra(0)
