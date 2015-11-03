import Queue
import Stack 
import Tree
import Graph
import random

def main():
	print "\n===Testing Queue implementation==="
	Q = Queue.Queue()
	print "Enqueueing numbers 0 to 9"
	for i in range(0,10):
		Q.put(i)
	print "Dequeueing all elements"
	for i in range(0,10):
		print "\t%d" % Q.get()

	print "\n===Testing Stack implementation==="
	S = Stack.Stack()
	print "Adding numbers 0 to 9"
	for i in range(0,10):
		S.push(i)
	print "Popping all elements off the stack"
	for i in range(0,10):
		print "\t%d" % S.pop()

	print "\n===Testing Binary Tree implementation==="
	T = Tree.Tree()
	print "Adding 10 items to the tree"
	T.add(1,None)
	T.add(2,1)
	T.add(3,1)
	T.add(4,1) #This expected to not work
	T.add(4,2)
	T.add(5,3)
	T.add(6,3)
	T.add(7,4)
	T.add(8,4)
	T.add(9,5)
	T.printTree()
	print "Deleting 2 items from the tree"
	T.delete(6)
	T.delete(3) #This expected to not work
	T.printTree()

	print "\n===Testing Graph implementation==="
	G = Graph.Graph()
	print "Adding 10 vertecies to the graph"
	for i in range(0,10):
		G.addVertex(i)
	print "Adding 20 edges to the graph"
	for i in range(0,20):
		G.addEdge(random.randint(0,9),random.randint(0,9))
	print "Finding 5 vertecies in the graph"
	for i in range(0,10):
		print "vertex %d has the following edges: " %i
		print G.vertecies[i]



main()
