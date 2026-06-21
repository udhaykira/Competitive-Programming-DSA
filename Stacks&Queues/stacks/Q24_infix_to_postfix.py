"""
Problem : Convert an Infix Expression into a Postfix Expression.

## What is Infix?

Operator is between operands.

```
A + B

A + B * C

(A+B) * C

```

---

## What is Postfix?

Operator comes after operands.

```
AB+

ABC*+

AB+C*

"""

def infixToPostfix(exp):
    stack = []
    ans = []
    
    priority = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }
    
    for ch in exp:
        if ch.isalnum():
            ans.append(ch)
        
        elif ch == '(':
            stack.append(ch)
        
        elif ch == ')':
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            if stack:
                stack.pop()
        
        elif ch in priority:
            while stack and stack[-1] != '(':
                top_op = stack[-1]
                if (ch == '^' and priority[ch] < priority[top_op]) or (ch != '^' and priority[ch] <= priority[top_op]):
                    ans.append(stack.pop())
                else:
                    break
            stack.append(ch)
            
    while stack:
        ans.append(stack.pop())
    
    return "".join(ans)