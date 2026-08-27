class Solution:
    def largest(self, arr):
        largest = arr[0]
        for i in range(len(arr)):
            if arr[i]> largest:
                largest = arr[i]
        return largest
        
        
