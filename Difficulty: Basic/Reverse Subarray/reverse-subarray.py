class Solution:
	def reverseSubArray(self,arr,l,r):
		l -=1 
		r -=1
		def rec(l,r):
		    if l >= r:
		        return
		    arr[l], arr[r] = arr[r], arr[l]
	    	return rec(l+1, r-1)
		rec(l,r)
		return arr
		