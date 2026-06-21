"""
Problem : Prefix Evaluation

# What is Prefix?

Operator comes before operands.

Example:

```
+ 2 3
```

means

```
2 + 3
```

Answer:

```
5
```

"""

def evaluatePrefix(exp):

	stack= []
	
	for token in reversed(exp):
	
		if token not in "+-*/":
			stack.append(int(token))
		
		else:
		
			a = stack.pop()
			b = stack.pop()
			
			if token == '+':
				stack.append(a+b)
			
			elif token == '-':
				stack.append(a-b)
			
			elif token == '*':
				stack.append(a*b)
			
			else:
				stack.append(int(a/b))
	
	return stack[0]