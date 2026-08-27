class Solution:
    def getSecondLargest(self, arr):
        largest = arr[0]
        secLargest = -1
        for i in range(1,len(arr)):
            if arr[i]>largest:
                secLargest = largest
                largest = arr[i]
            else:
                if arr[i]< largest and arr[i] > secLargest:
                    secLargest = arr[i]
        return secLargest
                