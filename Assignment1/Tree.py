class TreeNode:
	def __init__(self, value, parentNode):
		self.key = value
		self.leftChild = None
		self.rightChild = None
		self.parent = parentNode

class Tree:
	def __init__(self):
		self.root = None;

	def add(self, value, parentValue):
		if parentValue == None and self.root == None:
			self.root = TreeNode(value, parentValue)
		else:
			parent = self.search(parentValue) 
			if parent != None:
				if parent.leftChild == None and parent.rightChild == None:
					parent.leftChild = TreeNode(value, parent)
				elif parent.leftChild != None and parent.rightChild == None:
					parent.rightChild = TreeNode(value, parent)
				elif parent.leftChild != None and parent.rightChild != None:
					print "Parent has two children, node not added"
			else:
				print "Parent not found"
	
	#Recursive search function
	def search(self, value):
		if(self.root != None):
			return self._search(value, self.root)

	def _search(self, value, node):
		if node != None:
			if value == node.key:
				return node
			else:
				LSearch = self._search(value, node.leftChild)
				RSearch = self._search(value, node.rightChild)
				if LSearch != None:
					return LSearch
				elif RSearch != None:
					return RSearch

	def delete(self, value):
		node = self.search(value)
		parent = None
		if node != None:
			if node.leftChild == None and node.rightChild == None:
				parent = node.parent
				if parent.leftChild == value:
					parent.leftChild = None
				else:
					parent.rightChild = None
				node.parent == None
			else:
				print "Node not deleted, has children"
		else:
			print "Node not found"

	#Recursive pre-order Print function
	def printTree(self):
		if self.root != None:
			self._printTree(self.root)
		else:
			print "Tree is empty"

	def _printTree(self, node):
		if node != None:
			print "%d " % node.key
			self._printTree(node.leftChild)
			self._printTree(node.rightChild)
