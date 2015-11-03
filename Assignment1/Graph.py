class Graph:
	#Genertic initiator that has 1 class value of the dictionary
	def __init__(self):
		self.vertecies = dict()

	#Adds a vertex to the dictionary with an empty list associated to the key
	def addVertex(self, value):
		if value not in self.vertecies:
			self.vertecies.update({value : []})
		else:
			print "Vertex already exists"

	#Adds the edge value between 2 vertex by appending the list associated with
	#each key
	def addEdge(self, value1, value2):
		if value1 not in self.vertecies or value2 not in self.vertecies:
			print "One or more vertices not found"
		else:
			if value1 == value2:
				return
			if value2 not in self.vertecies[value1]:
				self.vertecies[value1].append(value2)
			if value1 not in self.vertecies[value2]:
				self.vertecies[value2].append(value1)

	#Prints all edges associated with a vertex
	def findVertex(self, value):
		print "Vertex %d has the following edges: " %value
		print self.vertecies[value]
