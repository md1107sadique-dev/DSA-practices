class Solution:
    def maxSubarraySum(self, arr):
        subarray = float("-inf")
        total = 0
        n = len(arr)
        for i in range(n):
            total += arr[i]
            if subarray< total:
                subarray = total
            if total < 0:
                total = 0
        return subarray