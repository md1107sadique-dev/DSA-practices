class Solution:
    def countFreq(self, arr, target):
        
        def lp(arr, target):
            n = len(arr)
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high)//2
                if arr[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low
        def up(arr, target):
            n = len(arr)
            low = 0
            high = n-1
            while low <= high:
                mid = (low + high)//2
                if arr[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low
        first = lp(arr,target)
        last = up(arr, target)
        
        if first == len(arr) or arr[first] != target:
            return 0
        return last - first