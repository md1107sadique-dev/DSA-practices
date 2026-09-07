class Solution:
	def pushZerosToEnd(self, arr):
	    n = len(arr)
	    if n == 0:
    	    return
    	i = 0
    	while i < n:
    	    if arr[i] == 0:
    	        break
    	    i += 1
        if i == n:
            return arr
        j = i + 1
        while j < n:
            if arr[j] != 0:
                arr[i],arr[j] = arr[j], arr[i]
                i += 1
            j += 1