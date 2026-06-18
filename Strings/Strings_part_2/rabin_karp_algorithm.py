"""
Question:

Given a text string and a pattern string, return True if the pattern
exists in the text using the Rabin-Karp Algorithm, otherwise return False.

Input:
text = "xabcz"
pattern = "abc"

Output:
True

Explanation:
Text windows of size 3:
"xab" -> No match
"abc" -> Match found

Hence return True.
"""


class Solution:

    @staticmethod
    def rabin_karp(text, pattern):

        n = len(text)
        m = len(pattern)

        # Pattern longer than text cannot exist
        if m > n:
            return False

        base = 31

        # Calculate base^(m-1)
        highest_power = 1
        for _ in range(m - 1):
            highest_power *= base

        pattern_hash = 0
        window_hash = 0

        # Compute hash of pattern and first window
        for i in range(m):
            pattern_hash = pattern_hash * base + ord(pattern[i])
            window_hash = window_hash * base + ord(text[i])

        # Slide window through text
        for i in range(n - m + 1):

            # If hashes match, verify actual strings
            if pattern_hash == window_hash:
                if text[i:i + m] == pattern:
                    return True

            # Compute hash for next window
            if i < n - m:
                window_hash -= ord(text[i]) * highest_power
                window_hash = window_hash * base + ord(text[i + m])

        return False


# Input
text = "xabcz"
pattern = "abc"

# Output
print(Solution.rabin_karp(text, pattern))

# Expected Output:
# True