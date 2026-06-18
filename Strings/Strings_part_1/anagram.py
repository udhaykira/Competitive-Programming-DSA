"""
LeetCode : 242
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1!=n2:
            return False
        c = [0]*26
        for i in range(n1):
            c[ord(s[i])-ord('a')]+=1
            c[ord(t[i])-ord('a')]-=1
        for i in c:
            if i!=0:
                return False
        return True

# Example usage:
solution = Solution()
s = "anagram"
t = "nagaram"
print(solution.isAnagram(s, t))  # Output: True


        