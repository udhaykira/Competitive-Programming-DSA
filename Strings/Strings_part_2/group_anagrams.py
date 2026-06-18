"""
LeetCode : 49
Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""

class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in d:
                d[sorted_word].append(word)
            else:
                d[sorted_word] = []
                d[sorted_word].append(word)
        res = []
        # print(d)
        for k in d:
            res.append(d[k])
        return res

# Example usage:
solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]