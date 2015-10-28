class Stack():
	def __init__(self):
		self.stack = []

	def push(self, ele):
		self.stack.append(ele)
	def size(self):
		return len(self.stack)
	def pop(self):
		if self.empty():
			raise Exception("no element")
		else:
			return self.stack.pop()
	def empty(self):
		return self.size() == 0
	def top(self):
		return self.stack[self.size()-1]

	def clear(self):
		del self.items[:]
