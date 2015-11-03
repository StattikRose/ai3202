#Jennifer Dooley
#830371622
#Assignment 3 CSCI3202

from sys import argv
import math

WIDTH = 10
HEIGHT = 8

class Node:
	def __init__(self, val):
		#map value
		self.val = int(val)
		#location values
		self.x = 0
		self.y = 0
		self.parent = None
		#A* search cost values
		self.h = 0
		self.g = 0
		self.f = 0

	def setLoc(self, x ,y):
		self.x = x
		self.y = y

def getGraph(fin, graph, height):
	index = 0
	#Done so that the start will be at 0,0
	y = height-1
	for line in fin:
		if line:
			x = 0
			#split input and assign value to each location on grid
			lineSplit = line.split()
			for val in lineSplit:
				n = Node(val)
				n.setLoc(x,y)
				graph.addData(n, index)
				x += 1
			y -= 1
			index += 1

class Graph:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		#creates a 2D array
		self.data = []
		for i in range(0,height):
			self.data.append([])

	def addData(self, node, index):
		self.data[index].append(node)

	def getNode(self, x, y):
		#make sure node exists
		if x < 0 or y < 0:
			return None
		#find and return node
		else:
			for i in self.data:
				for node in i:
					if node.x == x and node.y == y:
						return node

	#return all neighbor nodes for given node
	def neighbors(self, node):
		neighbors = []
		x = node.x
		y = node.y

		#find all possible neighbors (8 possible)
		North = self.getNode(x,y+1)
		East = self.getNode(x+1,y)
		West = self.getNode(x-1,y)
		South = self.getNode(x,y-1)
		NorthEast = self.getNode(x+1,y+1)
		NorthWest = self.getNode(x-1,y+1)
		SouthEast = self.getNode(x+1,y-1)
		SouthWest = self.getNode(x-1,y-1)

		#set costs to move
		for node in [North, East, West, South, NorthEast, NorthWest, SouthEast, SouthWest]:
			if node is not None and node.val is not 2:
				cost = 0
				if node in [North, East, West, South]:
					cost = 10
				else:
					cost = 14
			#add 10 if mountain
				if node.val is 1:
					cost += 10
				neighbors.append([node,cost])
		return neighbors

	#overload call for neighbors to handle being called with co-ords
	def _neighbors(self, x, y):
		node = self.get(x,y)
		return neighbors(self,node)

	#used for troubleshooting reading in the graph
	def printGraph(self):
		for x in range(self.height):
			line = ""
			for y in range(self.width):
				line += str(self.data[x][y].val) + " "
			print line

class Search:
	#prevents infinite loops
	MAXPATH = 100

	def __init__(self, start, goal, graph, heuristic):
		self.path = []
		self.start = start
		self.goal = goal
		self.heuristicChoice = heuristic
		self.graph = graph
		self.numEval = 1

	def manhattan(self, node):
		dx = abs(node.x - self.goal.x)
		dy = abs(node.y - self.goal.y)
		return 10 * (dx + dy)

	def euclidean(self, node):
		dx = abs(node.x - self.goal.x)
		dy = abs(node.y - self.goal.y)
		return 10 * math.sqrt(dx**2 + dy**2)

	def heuristic(self, node):
		if self.heuristicChoice == "manhattan":
			return self.manhattan(node)
		else:
			return self.euclidean(node)

	#updates parent and cost of node
	def update(self, node, parent, cost):
		node.parent = parent
		node.g = cost + parent.g
		node.h = self.heuristic(node)
		node.f = node.g + node.h

	def printSearch(self):
		path = self.getPath(self.goal)
		print "==========Results=========="
		print "Heuristic: %s" %self.heuristicChoice
		print "Cost of path: %d" %self.goal.f
		print "Number of nodes visited: %d" %self.numEval
		print "Path: \n %s" %path
		print "==========================="

	def aStar(self):
		openList = [self.start]
		closedList = []

		while len(openList) > 0:
			node = min(openList, key=lambda n: n.f)
			openList.remove(node)
			if node != self.goal:
				closedList.append(node)
				for (neighbor, cost) in self.graph.neighbors(node):
					if neighbor not in closedList:
						if neighbor in openList:
							if neighbor.g > (node.g + cost):
								self.update(neighbor, node, cost)
						else:
							self.update(neighbor, node, cost)
							openList.append(neighbor)
							self.numEval += 1
			else:
				self.printSearch()
				break		

	#returns path of search
	def getPath(self, node):
		path = []
		next = node
		for i in range(0, self.MAXPATH):
			if next:
				path.append((next.x,next.y))
				next = next.parent
		return path[::-1]

		
if __name__ == "__main__":
	fin = open(argv[1])
	g = Graph(WIDTH,HEIGHT)

	getGraph(fin,g,HEIGHT)
	
	s = Search(g.getNode(0,0), g.getNode(WIDTH-1,HEIGHT-1), g, argv[2])
	s.aStar()
