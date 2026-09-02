class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        # freq = {}

        # O(2N)-- not optimal 

        # for i in range(n):
        #     freq[nums[i]] = freq.get(nums[i],0)+1
        # m = len(freq)
        # for x, num in enumerate(freq):
        #     nums[x] = num
        # return m

        # Brute force 
        # for i in range(n):
        #     freq[nums[i]] = 0
        # j = 0
        # for i in freq:
        #     nums[j] = i
        #     j+=1
        # return j

        # Optimal solution

        if n == 1:
            return 1
        i = 0
        j = i + 1
        while j < n:
            if nums[i] != nums[j]:
                i+=1
                nums[i],nums[j] = nums[j], nums[i]
            j += 1
        return i + 1
        
        