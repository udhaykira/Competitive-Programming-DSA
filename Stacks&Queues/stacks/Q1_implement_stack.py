class Stack:

		def __init__(self):
				self.stack= []
		
		def push(self, x):
				self.stack.append(x)
	
		def pop(self):
				if self.empty():
					return None
				return self.stack.pop()
	
		def top(self):
				if self.empty():
					return None
				return self.stack[-1]
		
		def empty(self):
				return len(self.stack)==0
	

# Example
s=Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.top())# 30
print(s.pop())# 30
print(s.top())# 20
print(s.empty())# False