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
    def checkInclusion(self, s1, s2):
        d1 = {}
        for i in s1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        k = len(s1)
        for i in range(len(s2)-k+1):
            curr = s2[i:i+k]
            d2 = {}
            for j in curr:
                if j in d2:
                    d2[j]+=1
                else:
                    d2[j]=1
            if d1 == d2:
                return True
        return False

# Example usage:
solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(solution.checkInclusion(s1, s2))  # Output: True
        