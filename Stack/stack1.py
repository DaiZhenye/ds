class StackUnderflow(ValueError): #栈下溢
	pass

class SStack():
	def __init__(self):
		self._elems = []
		
	def is_empty(self):
		return self._elems == []
	
	def top(self):
		if self._elems == []:
			raise StackUnderflow("in SStack.top()")
		return self._elems[-1]
	
	def push(self,elem):
		self._elems.append(elem)
		
	def pop(self):
		if self._elems == []:
			raise StackUnderflow("in SStack.pop()")
		return self._elems.pop()
		
	