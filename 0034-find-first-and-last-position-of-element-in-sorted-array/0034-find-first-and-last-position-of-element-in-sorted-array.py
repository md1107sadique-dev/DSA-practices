class Solution(object):
    def searchRange(self, nums, target):
        def lowest(nums,target):
            n = len(nums)
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if  nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low
        def upper(nums, target):
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            return low
        first = lowest(nums,target)
        last = upper(nums,target)
        if first == len(nums) or nums[first] != target:
            return [-1,-1]
        return [first,last-1]
        