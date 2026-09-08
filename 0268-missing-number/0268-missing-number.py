class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total_sum = n*(n+1)//2
        sum = 0
        for i in range(n):
            sum += nums[i]
        missingNum = total_sum - sum
        return missingNum
        