"""
LeetCode : 1209
Remove All Adjacent Duplicates in String II

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1][0]==ch:
                stack[-1][1]+=1
            else:
                stack.append([ch,1])
            if stack[-1][1]==k:
                stack.pop()
        result = []
        for char, count in stack:
            result.append(char*count)
        return "".join(result)
        