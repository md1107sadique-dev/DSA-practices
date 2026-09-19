class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        low = 0
        high = n-1
        # Itrative
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

        # Rcursive solution
        # def bs(low, high):
        #     if low > high:
        #         return -1
        #     mid = (low + high)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         return bs(mid+1,high)
        #     else:
        #         return bs(low,mid-1)
        # return bs(low,high)
            
        