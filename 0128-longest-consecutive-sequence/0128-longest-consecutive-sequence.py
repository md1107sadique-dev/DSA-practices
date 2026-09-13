class Solution(object):
    def longestConsecutive(self, nums):
        freq = {}
        n = len(nums)
        for i in range(n):
            freq[nums[i]] = freq.get(nums[i],0)
        max_count = 0
        for num in freq:
            if num -1 not in freq:
                count = 1
                next_count = num +1
                while next_count in freq:
                    count +=1
                    next_count +=1
                max_count = max(max_count, count)
        return max_count
            

        
        