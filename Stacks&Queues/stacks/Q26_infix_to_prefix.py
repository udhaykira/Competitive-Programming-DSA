"""
Problem : Convert an Infix Expression into a Prefix Expression.

# What is Prefix?

Infix : A + B
Operator in the middle.

Prefix : +AB
Operator comes first.

Example 1

Input : A+B*C

Meaning: A + (B*C)

Prefix : +A*BC

"""
def infixToPrefix(exp):

	exp = exp[::-1]
	
	temp= []
	
	for ch in exp:
		if ch=='(':
			temp.append(')')
		elif ch==')':
			temp.append('(')
		else:
			temp.append(ch)
	
	exp = "".join(temp)
	
	stack = []
	ans = []
	
	priority= {
		'+':1,
		'-':1,
		'*':2,
		'/':2,
		'^':3
  }
	
	for ch in exp:
	
		if ch.isalnum():
			ans.append(ch)
		
		elif ch == '(':
			stack.append(ch)
		
		elif ch == ')':
		
			while stack and stack[-1]!='(':
				ans.append(stack.pop())
		
			stack.pop()
		
		else:
		
			while (stack and stack[-1]!='(' and priority[stack[-1]]>=priority[ch]):
				ans.append(stack.pop())
			
			stack.append(ch)
	
	while stack:
		ans.append(stack.pop())
	
	return "".join(ans)[::-1]