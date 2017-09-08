ADT Queue:
	Queue(self)
	is_empty(self)
	enqueue(self,elem)
	dequeue(self)
	peek(self)

实现：
链接表技术实现队列
最简单的单链表只支持首端的高效操作（忘记为什么了）
带表尾端指针的单链表，支持O(1)时间的尾端插入操作

队列的顺序表实现：
循环顺序表