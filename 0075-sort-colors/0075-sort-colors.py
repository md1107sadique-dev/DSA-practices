class Solution(object):
    def sortColors(self, nums):
        def partition(l,r):
            if l >= r:
                return
            pivot = nums[l]
            i = l
            j = r
            while i < j:
                while i <= r and nums[i] < pivot:
                    i+=1
                while j >= l and nums[j] > pivot:
                    j-=1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i +=1
                    j-=1
            
            partition(l,j)
            partition(i,r)
        n = len(nums)-1
        partition(0,n)
       
        