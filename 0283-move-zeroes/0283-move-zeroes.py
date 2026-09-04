class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        if n==1:
            return
        i = 0
        
        # m-1 (Brute Force) 
        # while i < n:
        #     if nums[i] == 0:
        #         temp = nums[i]
        #         for j in range(i,n-1):
        #             nums[j] = nums[j+1]
        #         nums[n-1] = temp
        #         n -= 1
        #     if nums[i] != 0:
        #         i +=1

        # m-2(optimal)
        # j = 0
        # while i < n:
        #     if nums[i] != 0 and nums[j]==0:
        #         nums[i],nums[j] = nums[j],nums[i]
        #         j+=1
        #     elif nums[j]!=0:
        #         j+=1
        #     i+=1


        # m-3(Optimal)--> best and clear
        while i < n:
            if nums[i] == 0:
                break
            i+=1
        j =i+1
        while j < n:
            if nums[j]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
            j+=1