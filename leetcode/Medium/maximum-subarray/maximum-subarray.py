class Solution(object):
    def maxSubArray(self, nums):
        second = float("-inf")
        n = len(nums)
        
        # m-1(Brute force)
        # for i in range(n):
        #     sum = nums[i]
        #     if sum > second:
        #         second = sum 
        #     for j in range(i+1,n):
        #         sum += nums[j]
        #         if sum > second:
        #             second = sum
        #     sum = 0

        # m-2(Optimal)
        total = 0
        for i in range(n):
            total += nums[i]
            if second < total:
                second = total
            if total < 0:
                total = 0
            
        return second