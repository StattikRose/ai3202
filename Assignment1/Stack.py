class Stack:
	#Class functions
	def __init__(self):
		self.st = []
		self.size = 0

	def push(self, x):
		#treats the end of the list as if it were the top of the stack
		#adds the object x to the end of the list
		#increments the stack size by 1
		self.st.append(x)
		self.size = self.size + 1

	def pop(self):
		#treats the end of the list as if it were the top of the stack
		#saves the top object in the stack to output
		#deletes the item from the list
		#decrements the stack size and returns output
		output = self.st[self.checkSize() - 1]
		del self.st[self.checkSize() - 1]
		self.size = self.size - 1
		return output

	def checkSize(self):
		#returns stack size
		return self.size
