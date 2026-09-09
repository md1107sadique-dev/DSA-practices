class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)

        # m-1(Brute force)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         sum = nums[i] + nums[j]
        #         if sum == target:
        #             return [i,j]
        

        # m-2(Optimal)
        freq = {}
        for i in range(n):
            remaning = target - nums[i]
            if remaning in freq:
                return [freq[remaning],i]
            freq[nums[i]] = i