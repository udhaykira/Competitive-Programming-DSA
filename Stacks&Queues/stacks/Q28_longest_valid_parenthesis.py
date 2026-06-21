"""
LeetCode : 32
Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for idx, ch in enumerate(s):
            if ch=='(':
                stack.append(idx)
            else:
                stack.pop()
            if stack:
                max_len = max(max_len, idx-stack[-1])
            else:
                stack.append(idx)
        return max_len
        