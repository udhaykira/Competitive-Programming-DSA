"""
LeetCode : 402
Remove K Digits

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while stack and stack[-1]>ch and k>0:
                stack.pop()
                k-=1
            stack.append(ch)

        while k>0:
            stack.pop()
            k-=1

        result = "".join(stack).lstrip("0")
        return result if result else "0"