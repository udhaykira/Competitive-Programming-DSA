"""
LeetCode : 387
First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0

Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for ch in s:
            count[ch] = count.get(ch,0) + 1
        for idx,char in enumerate(s):
            if count[char]==1:
                return idx
        return -1


        