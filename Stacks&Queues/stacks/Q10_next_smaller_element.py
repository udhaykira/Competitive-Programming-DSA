"""
Problem : Next Smaller Element

For every element in the array, find the **first smaller element to its right**.

If no smaller element exists, return `-1`.

"""

def nextSmaller(nums):
	n = len(nums)
	ans= [-1]*n
	stack= []
	
	for i in range(n-1,-1,-1):
		while stack and stack[-1]>=nums[i]:
			stack.pop()
		
		if stack:
			ans[i] = stack[-1]
		
		stack.append(nums[i])
	
	return ans