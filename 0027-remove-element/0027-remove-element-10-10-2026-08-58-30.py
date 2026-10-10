class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[j] == val:
                j-=1
            elif nums[j] != val and nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                i += 1
            else:
                i +=1
        return i
                

