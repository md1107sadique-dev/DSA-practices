class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        arr = []
        for i in range(0,n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                z = n-1
                while k < z:
                    total = nums[i]+nums[j]+nums[k]+nums[z]
                    if total == target:
                        fourth = [nums[i],nums[j],nums[k],nums[z]]
                        arr.append(fourth)
                        k+=1
                        z-=1
                        while k < z and nums[k] == nums[k-1]:
                            k += 1
                        while k < z and nums[z] == nums[z+1]:
                            z -= 1    
                    elif total < target:
                        k+=1
                    else:
                        z-=1
        return arr