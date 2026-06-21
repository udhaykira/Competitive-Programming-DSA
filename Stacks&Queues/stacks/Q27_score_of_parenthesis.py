"""
LeetCode : 856
Score of Parentheses

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 
Example 1:

Input: s = "()"
Output: 1

Example 2:

Input: s = "(())"
Output: 2

Example 3:

Input: s = "()()"
Output: 2
 
"""
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for idx, char in enumerate(s):
            if char=='(':
                stack.append(score)
                score = 0
            else:
                if s[idx-1]=='(':
                    score = stack.pop() + 1
                else:
                    score = stack.pop() + 2*score
        return score
        