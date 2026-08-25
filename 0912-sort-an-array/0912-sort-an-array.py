class Solution(object):
    def sort(self,left, right):
        temp = []
        i, j = 0,0
        n, m = len(left), len(right)
        while i < n and j < m:
            if left[i] <= right[j]:
                temp.append(left[i])
                i+=1
            else:
                temp.append(right[j])
                j+=1
        while i < n:
            temp.append(left[i])
            i+=1
        while j < m:
            temp.append(right[j])
            j+=1
        return temp
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left_half = nums[:mid]
        right_half = nums[mid:]
        left = self.sortArray(left_half)
        right = self.sortArray(right_half)
        return self.sort(left, right)
        
        