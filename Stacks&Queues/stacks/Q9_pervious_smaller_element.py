"""
Problem : Previous Smaller Element

For every element in the array, find the **first smaller element to its left**.

If no smaller element exists, return `-1`.

"""

def previousSmaller(nums):
    stack= []
    ans= []
    
    for num in nums:
        while stack and stack[-1]>=num:
            stack.pop()
    
            if stack:
                    ans.append(stack[-1])
            else:
                    ans.append(-1)
            
            stack.append(num)
    
    return ans