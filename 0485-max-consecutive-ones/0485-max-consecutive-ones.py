class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        largest_count = 0
        n = len(nums)
        for i in nums:
            if i == 1:
                count += 1
                if count > largest_count:
                    largest_count = count
            else:
                count = 0
        return largest_count
                 
        