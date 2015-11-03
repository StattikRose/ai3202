#Jennifer Dooley
#830371622
#Assignment 5 CSCI3202

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
		#Markov utility and reward values
		#set based on map value

		#Empty square
		if self.val is 0:
			self.reward = 0
			self.util = 0
		#Mountain square
		elif self.val is 1:
			self.reward = -1
			self.util = -1
		#Wall square
		elif self.val is 2:
			self.reward = None
			self.util = None
		#Snake square
		elif self.val is 3:
			self.reward = -2
			self.util = -2
		#Barn square
		elif self.val is 4:
			self.reward = 1
			self.util = 1
		#Goal square
		elif self.val is 50:
			self.reward = 50
			self.util = 50

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
	def __init__(self, width, height, e, discount):
		self.width = width
		self.height = height
		self.E = float(e)
		self.discount = float(discount)
		#creates a 2D array
		self.data = []
		for i in range(0,height):
			self.data.append([])

	def addData(self, node, index):
		self.data[index].append(node)

	def getNode(self, x, y):
		#make sure node exists
		if x < 0 or y < 0 or x >= WIDTH or y >= HEIGHT:
			return None
		#find and return node
		else:
			for i in self.data:
				for node in i:
					if node.x == x and node.y == y:
						return node

	#Sets util for all nodes
	def setUtils(self):
		change = 100
		while change >= self.E * (1-self.discount)/self.discount:
			change = -100
			for i in range(0, self.width):
				for j in range(0, self.height):
					center = self.getNode(i,j)
					North = self.getNode(i,j+1)
					East = self.getNode(i+1,j)
					West = self.getNode(i-1,j)
					South = self.getNode(i,j-1)

					if center.util is not None and center.val is not 50:
						northUtil = None
						eastUtil = None
						westUtil = None
						southUtil = None

						if North is None or North.util is None:
							northUtil = center.util
						else:
							northUtil = North.util
						if East is None or East.util is None:
						    eastUtil = center.util
						else:
						    eastUtil = East.util
						if West is None or West.util is None:
						    westUtil = center.util
						else:
						    westUtil = West.util
						if South is None or South.util is None:
							southUtil = center.util
						else:
							southUtil = South.util

						moveNorth = .8*northUtil + .1*eastUtil + .1*westUtil
						moveEast = .8*eastUtil + .1*southUtil + .1*northUtil
						moveWest = .8*westUtil + .1*northUtil + .1*southUtil
						moveSouth = .8*southUtil + .1*westUtil + .1*eastUtil
						prevUtil = center.util
						center.util = max(moveNorth, moveEast, moveWest, moveSouth) + center.reward
						center.util = center.util*self.discount

						if abs(center.util - prevUtil) > change:
							change = abs(center.util - prevUtil)

	#used for troubleshooting reading in the graph
	def printGraph(self):
		for x in range(self.height):
			line = ""
			for y in range(self.width):
				line += str(self.data[x][y].val) + " "
			print line

class Search:
	def __init__(self, start, goal, graph):
		self.path = []
		self.utils = []
		self.start = start
		self.goal = goal
		self.graph = graph

	#returns most optimal path of search
	def getPath(self):
		self.graph.setUtils()
		self.path.append(self.start)
		self.utils.append(self.start.util)
		current = self.start

		while current is not self.goal:
			North = self.graph.getNode(current.x, current.y+1)
			East = self.graph.getNode(current.x+1, current.y)
			West = self.graph.getNode(current.x-1, current.y)
			South = self.graph.getNode(current.x, current.y-1)

			northUtil = None
			eastUtil = None
			westUtil = None
			southUtil = None

			if North == None:
				northUtil = float('-inf')
			else:
				northUtil = North.util
			if South == None:
				southUtil = float('-inf')
			else:
				southUtil = South.util
			if West == None:
				westUtil = float('-inf')
			else:
				westUtil = West.util
			if East == None:
				eastUtil = float('-inf')
			else:
				eastUtil = East.util

			if northUtil == max(northUtil, southUtil, westUtil, eastUtil):
				current = North
			elif eastUtil == max(northUtil, southUtil, westUtil, eastUtil):
				current = East
			elif westUtil == max(northUtil, southUtil, westUtil, eastUtil):
				current = West
			elif southUtil == max(northUtil, southUtil, westUtil, eastUtil):
				current = South

			self.path.append(current)
			self.utils.append(current.util)

	def printSearch(self):
		self.getPath()
		print "==========Results=========="
		print "Path: "
		for item in self.path:
			print "(%d,%d)" %(item.x,item.y),
		print "\nUtility of path: " 
		for item in self.utils:
			print "%.2f" %item,
		print "\n==========================="

if __name__ == "__main__":
	fin = open(argv[1])
	g = Graph(WIDTH,HEIGHT, argv[2], .9)

	getGraph(fin,g,HEIGHT)

	s = Search(g.getNode(0,0), g.getNode(WIDTH-1,HEIGHT-1), g)
	s.printSearch()
