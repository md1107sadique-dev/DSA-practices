class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        freq = {}
        ans = []
        for i in range(n):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        keys = []
        for k in freq:
            keys.append(k)
        keys.sort()
        while len(ans) < n:
            for k in keys:
                if freq[k] > 0:
                    ans.append(k)
                    freq[k] = freq[k] - 1

        return ans
                
        