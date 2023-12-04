######################### 
# Course: COMP 2113 FA01, 2023
# Assignment 8 - Graphs and Graph Traversal
# Author: Cameron Bender
# Student ID: 0301563b
# email address: 0301563b@acadiau.ca
# Date: 2023/11/21
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################

from collections import deque

class Graph:
    
    #Constructor
    def __init__(self):
        self.vertices = {}
    
    #Add vertex function
    def addVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    
    #Add edge function
    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
    
    #Function to determine neighbours of a given node
    def outEdges(self, vertex):
        return self.vertices.get(vertex, [])
    
    #List of vertices who have that vertex as a neighbour
    def inEdges(self, vertex):
        inEdges_list = []
        for v, edges in self.vertices.items():
            if vertex in edges:
                inEdges_list.append(v)
        return inEdges_list
    
    #Print the graph!
    def printGraph(self):
        for vertex, edges in self.vertices.items():
            edgesStr = ", ".join(edges)
            print(f"Node {vertex} is connected to: {edgesStr}")
            
            
            
    #DFS
    def dfs(self, startVertex, visited=None):
        # If visited set is not provided, initialize it as an empty set
        if visited is None:
            visited = set()
        # Mark the current vertex as visited
        visited.add(startVertex)
        print(f"Visited: {startVertex}")
        # Explore neighbours using recursion
        for neighbour in self.outEdges(startVertex):
            # If neighbour is not visited, recursively call DFS
            if neighbour not in visited:
                self.dfs(neighbour, visited)
    
    #BFS
    def bfs(self, startVertex):
        visited = set()
        # Initialize a deque with the starting vertex
        queue = deque([startVertex])
        # Mark the starting vertex as visited
        visited.add(startVertex)
        # BFS loop
        while queue:
            # Dequeue the leftmost vertex
            currentVertex = queue.popleft()
            print(f"Visited: {currentVertex}")
            for neighbour in self.outEdges(currentVertex):
                # If neighbour is not visited, mark it as visited and enqueue
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

                    
    def connectedComponents(self):
        #Create set for visited vertices and list for connected components
        visited = set()
        components = []
        
        #Iterate through vertices
        for vertex in self.vertices:
            #If not visited, make a new connected component
            if vertex not in visited:
                component = set()
                queue = deque([vertex])
                
                #Use BFS to exploer connected component
                while queue:
                    currentVertex = queue.popleft()
                    if currentVertex not in visited:
                        visited.add(currentVertex)
                        component.add(currentVertex)
                        queue.extend(neighbour for neighbour in self.outEdges(currentVertex) if neighbour not in visited)
                        
                #Add connected component to list 
                components.append(component)
                
        return components

    def shortestPath(self, startVertex, endVertex):
        queue = deque([(startVertex, [startVertex])])
        visited = set()

        while queue:
            currentVertex, path = queue.popleft()
            visited.add(currentVertex)
            
            #Explore neighbours of vertex 
            for neighbour in self.outEdges(currentVertex):
                if neighbour not in visited:
                    #Make a new path by connecting with neighbour
                    newPath = path + [neighbour]
                    queue.append((neighbour, newPath))
                    visited.add(neighbour)
                    
                    #If neighbour is the last vertex, return the path :)
                    if neighbour == endVertex:
                        return newPath

        return None  # No path found


if __name__ == "__main__":

    # Graph 1
    graph1 = Graph()
    
    #Creating vertices
    graph1.addVertex('A')
    graph1.addVertex('B')
    graph1.addVertex('C')
    graph1.addVertex('D')
    graph1.addVertex('E')
    graph1.addVertex('F')
    
    #Creating edges
    graph1.addEdge('A', 'B')
    graph1.addEdge('A', 'C')
    graph1.addEdge('B', 'C')
    graph1.addEdge('B', 'D')
    graph1.addEdge('C', 'D')
    graph1.addEdge('D', 'A')
    graph1.addEdge('E', 'F')
    graph1.addEdge('F', 'D')
    
    #Print graph
    print("Graph 1:")
    graph1.printGraph()
    
    #Print DFS
    print("\nDepth-First Search:")
    graph1.dfs('A')
    
    #Print BFS
    print("\nBreadth-First Search:")
    graph1.bfs('A')
    
    #Print connected components with a for loop
    print("\nConnected Components:")
    components1 = graph1.connectedComponents()
    for i, component in enumerate(components1, 1):
        print(f"Component {i}: {component}")
    
    #Shortest Path
    startVertex1 = 'A'
    endVertex1 = 'D'
    shortestPath1 = graph1.shortestPath(startVertex1, endVertex1)
    
    if shortestPath1:
        print(f"\nShortest Path from {startVertex1} to {endVertex1}: {shortestPath1}")
    else:
        print(f"\nNo path found from {startVertex1} to {endVertex1}.")

    # Graph 2
    graph2 = Graph()
    
    graph2.addVertex('X')
    graph2.addVertex('Y')
    graph2.addVertex('Z')
    
    graph2.addEdge('X', 'Y')
    graph2.addEdge('Y', 'Z')
    
    #Print graph
    print("\nGraph 2:")
    graph2.printGraph()
    
    #Print DFS
    print("\nDepth-First Search:")
    graph2.dfs('X')
    
    #Print BFS
    print("\nBreadth-First Search:")
    graph2.bfs('X')
    
    #Print connected components
    print("\nConnected Components:")
    components2 = graph2.connectedComponents()
    for i, component in enumerate(components2, 1):
        print(f"Component {i}: {component}")
    
    #Shortest Path
    startVertex2 = 'X'
    endVertex2 = 'Z'
    shortestPath2 = graph2.shortestPath(startVertex2, endVertex2)
    
    if shortestPath2:
        print(f"\nShortest Path from {startVertex2} to {endVertex2}: {shortestPath2}")
    else:
        print(f"\nNo path found from {startVertex2} to {endVertex2}.")
