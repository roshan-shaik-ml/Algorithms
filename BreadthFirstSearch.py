# Author: Shaik Faizan Roshan Ali
# Email: alsahercoder@gmail.com
# About: Graph Traversal Algorithm

from queue import Queue

class Graph:

    def __init__(self, edges, size):

        self.adjList = {}   
        self.size = size

        # creating the adjacency list
        for (src, dest) in edges:

            if(self.adjList.get(src) == None):

                self.adjList[src] = [dest]
            else:

                self.adjList[src].append(dest)
            
            if(self.adjList.get(dest) == None):

                self.adjList[dest] = [src]
            else:

                self.adjList[dest].append(src)         
    
    def BFS(self, start = None):

        if start == None:
            return
        
        visited = [False for _ in range(0, self.size)]
        queue = Queue(-1) # size of queue is infinity

        queue.put(start)
        visited[start] = True

        while(queue.empty() != True):

            current = queue.get()
            print(current, end = " ")

            for neighbour in self.adjList[current]:

                if(visited[neighbour] == False):
                    queue.put(neighbour)
                    visited[neighbour] = True

if __name__ == "__main__":

    edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
            (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)]
    
    size = 13 # no.of edges + 1
    graph = Graph(edges, size) # take the edges and no.of vertices + 1 as instance variable
    graph.BFS(1) # BFS takes the start node as parameter
