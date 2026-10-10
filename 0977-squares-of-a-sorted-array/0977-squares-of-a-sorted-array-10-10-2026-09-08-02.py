class Solution(object):
    def sortedSquares(self, nums):
        if len(nums) == 0:
            return nums
        result = [x**2 for x in nums]
        result.sort()
        return result      
        