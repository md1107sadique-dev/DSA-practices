class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Brute Force
        # for i in range(n):
        #     if nums[i] >=1 and nums[i] <= n:
        #         freq[nums[i]] = freq.get(nums[i],0)+1
        # for j in range(1,n+1):
        #     if j not in freq:
        #         return j

        # Optimal
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n :
                nums[i] = n + 4
        for i in range(0,n):
            num = abs(nums[i])
            if num > n:
                continue
            if nums[num-1] > 0:
                nums[num -1] = -nums[num -1]
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1