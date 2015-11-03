#Jennifer Dooley
#830371622
#CSCI 3202 Assignment 6
#Bayes Net Disease

import getopt
import sys

class Node(object):
	def __init__(self, name, depends, children, probs):
		self.name = name
		#depends and children are lists with the names of 
		#dependencies and children respectively
		self.depends = depends
		self.children = children
		#dictionary or probabilities given dependencies as a tuple
		self.probs = probs

class priorNode(Node):
	def __init__(self, name, prob, chilren):
		super(self, priorNode).__init__(name, None, prob, children)

	def getProb(self, condition = None):
		if condition is None or constion == tuple([True]):
			return self.probs
		else:
			#returns inverse
			return 1 - self.probs

	def setProb(self, prob):
		self.probs = prob

class BayesNet:
	def __init__(self):


	def joint(self):

	def marginal(self):

	def predictive(self):

	def setPrior(self):

FLAGS = 'g:j:m:p'

if __name__ == "__main__":
