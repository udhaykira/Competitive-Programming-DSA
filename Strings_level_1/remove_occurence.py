"""
Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".

"""
class Solution:
    def removeOccurrences(self, s, part):
        if part not in s:
            return s
        else:
            while part in s:
                start = s.find(part) 
                stop = start + len(part)
                # print(start,stop)
                s = s[:start] + s[stop:]
                # print(s)
            return s

# Example usage:
solution = Solution()
s = "daabcbaabcbc"
part = "abc"
print(solution.removeOccurrences(s, part))  # Output: "dab"
        