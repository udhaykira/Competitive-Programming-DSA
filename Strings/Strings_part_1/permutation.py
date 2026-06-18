"""
LeetCode : 567
Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m>n:
            return False
        ans = [0]*26
        for ch in s1:
            ans[ord(ch)-ord('a')]+=1
        cmp = [0]*26
        for ch in s2[:m]:
            cmp[ord(ch)-ord('a')]+=1
        for i in range(m,n):
            if cmp==ans:
                return True
            cmp[ord(s2[i-m])-ord('a')]-=1
            cmp[ord(s2[i])-ord('a')]+=1
        return cmp==ans

# Example usage:
solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(solution.checkInclusion(s1, s2))  # Output: True
        