class StackUnderflow(ValueError):
	pass

class SStack():
	def __init__(self):
		self._elems = []
		
	def is_empty():
		return self._elems == []
		
	def top():
		if self._elems == []:
			raise StackUnderflow("in SStack.top()")
		return self._elems[-1]
		
	def push(self,elem):
		self._elems.append(elem)
		
	def pop(self):
		if self._elems == []:
			raise StackUnderflow("in SStack.pop()")
		return self._elems.pop()

def suffix_exp_evaluator(line):
	print("suffix_exp_evaluator:执行")
	return suf_exp_evaluator(line.split())

#继承	
class ESStack(SStack):
	def depth(self):
		return len(self._elems)

def suf_exp_evaluator(exp):
	print("suf_exp_evaluator:执行")
	operators = "+-*/"
	st = ESStack()

	#continue语句告诉python跳出当前循环的剩余语句，然后继续执行下一轮循环
	#我们使用raise语句自己触发异常
	for x in exp:
		if x not in operators:
			st.push(float(x))
			print("st.push(float(%.2f))"%(float(x)))
			continue    #continue跳出本次循环，break跳出整个循环
		if st.depth() < 2:
			raise SyntaxError("short of operand(s).")
		print(st.depth())
		a = st.pop()
		print(a)
		b = st.pop()
		print(b)
		if x == "+":
			c = a + b
		elif x == "-":
			c = a - b
			print(c)
		elif x == "*":
			c = a * b
		elif x == "/":
			c = a / b
		else:
			break
		print("push")
		st.push(c)
		
	if st.depth() == 1:
		return st.pop()
	raise SyntaxError("Extra operand(s).")

def suffix_exp_calculator():
	while True:
		try:
			line = input("Suffix Expression:")
			if line == "end": return
			res = suffix_exp_evaluator(line)
			print(res)
		except Exception as ex:
			print("Error:",type(ex),ex.args)
		
