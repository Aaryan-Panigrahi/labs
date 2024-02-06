class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop() if self.items else None

	def peek(self):
		return self.items[-1] if self.items else None

	def is_empty(self):
		return not self.items


class MyQueue:
	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	def enqueue(self, item):
		self.s1.push(item)

	def dequeue(self):
		if self.s2.is_empty():

			while(not self.s1.is_empty()):
				temp = self.s1.pop()
				self.s2.push(temp)

		return self.s2.pop() if not self.s2.is_empty() else None

def main():
	q1 = MyQueue()
	q1.enqueue(2)
	q1.enqueue(3)

	print(q1.dequeue())

	q1.enqueue(7)
	q1.enqueue(8)
	print(q1.dequeue())
	print(q1.dequeue())
	print(q1.dequeue())

# def test_stack():
# 	s1 = Stack()
# 	s1.push(1)
# 	s1.push(2)
# 	s1.push(3)

# 	print(s1.pop())
# 	print(s1.pop())	
# 	print(s1.pop())

if __name__ == "__main__":
	# test_stack()
	main()


