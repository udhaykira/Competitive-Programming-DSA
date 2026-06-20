"""
LeetCode : 20
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

"""

class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack = []
        for i in s:
            if i in "{([":
                stack.append(i)
            else:
                if not stack or stack[-1]!=match[i]:
                    return False
                stack.pop()
        return True if not stack else False

        