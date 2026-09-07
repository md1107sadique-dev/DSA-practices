class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n
        def array(l,r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        array(0,d-1)
        array(d,n-1)
        array(0,n-1)