class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack = []
        for i in s:
            if i in "{([":
                stack.append(i)
            else:
                if not stack or stack[-1]!=match[i]:
                    return False
                stack.pop()
        return True if not stack else False

        