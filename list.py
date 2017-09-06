def test1():
	l = []
	for i in range(1000):
		l = l + [i]
		
def test2():
	l = []
	for i in range(1000):
		l.append(i)
		
def test3():
	l = [i for i in range(1000)]
	
def test4():
	l = list(range(1000))

t1 = Timer('test1()','from __main__ import test1')
print('concat',t1.timeit(number=10000),'milliseconds')
t2 = Timer('test2()','from __main__ import test2')
print('append',t2.timeit(number=10000),'milliseconds')
t3 = Timer('test3()','from __main__ import test3')
print('comprehensive',t3.timeit(number=10000),'milliseconds')
t4 = Timer('test4()','from __main__ import test4')
print('list range',t4.timeit(number=10000),'milliseconds')

'''
concat 60.02125106544577 milliseconds
append 3.7690841341769215 milliseconds
comprehensive 1.4450355941700082 milliseconds
list range 0.5656559530368668 milliseconds
'''

#测试pop操作：
x = list(range(2000000))
pop_zero = Timer('x.pop(0)','from __main__ import x')    //pop(i)  O(n)
print('pop_zero',pop_zero.timeit(number=10000),'milliseconds')
pop_zero 41.03826973938021 milliseconds
pop_end = Timer('x.pop()','from __main__ import x') // pop() O(1)
print('pop_end',pop_end.timeit(number=10000),'milliseconds')
pop_end 0.006304733121851314 milliseconds
