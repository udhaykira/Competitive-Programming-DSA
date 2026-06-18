"""
LeetCode : 76 
Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""
            
        t_count = {}
        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1
            
        t_chars = len(t_count)
        w_chars = 0
        w_count = {}
        left = 0

        min_len = float('inf')
        min_str = ""

        for right in range(m):
            char = s[right]
            w_count[char] = w_count.get(char, 0) + 1
            
            if char in t_count and t_count[char] == w_count[char]:
                w_chars += 1
                
            while t_chars == w_chars:
                left_char = s[left]
            
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_str = s[left:right+1]
                    
                w_count[left_char] -= 1
                
                if left_char in t_count and w_count[left_char] < t_count[left_char]:
                    w_chars -= 1
                    
                left += 1
                
        return min_str