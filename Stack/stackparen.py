class StackUnderflow(ValueError): #栈下溢
	pass

class SStack():
	def __init__(self):
		self._elems = []
		
	def is_empty(self):
		return self._elems == []
	
	def top(self):
		if self._elems == []:
			raise StackUnderflow("in SStack.top()") //raise 之后函数就结束执行了
		return self._elems[-1]
	
	def push(self,elem):
		self._elems.append(elem)
		
	def pop(self):
		if self._elems == []:
			raise StackUnderflow("in SStack.pop()")
		return self._elems.pop()

def check_parens(text):
	"""括号配对检查函数，text是被检查的正文串"""
	parens = "()[]{}"
	open_parens = "([{"
	opposite = {")":"(","]":"[","}":"{"}

	def parentheses(text):
		"""括号生成器，每次调用返回text里的下一括号及其位置"""
		i,text_len = 0,len(text)
		while True:
			while i < text_len and text[i] not in parens:
				i += 1
			if i >= text_len:
				return 
			print("yield前")
			yield text[i],i
			print("yield后")
			i += 1

	st = SStack()

	for pr,i in parentheses(text):
		print(pr,i)
		if pr in open_parens:
			st.push(pr)
		elif st.pop() != opposite[pr]:
			print("Unmatching is found at", i,"for",pr)
			return False
		else:
			pass
		
	print("All parentheses are correctly matched.")
	return True
		