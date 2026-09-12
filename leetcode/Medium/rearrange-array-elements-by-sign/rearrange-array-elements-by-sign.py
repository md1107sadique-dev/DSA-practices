class Solution(object):
    def rearrangeArray(self, nums):
        temp = []
        i = 0
        j = 0
        n = len(nums)
        if n == 0:
            return nums
        while i < n and j < n:
            k = len(temp)
            if k == 0:
                if nums[i]>=0:
                    temp.append(nums[i])
                i+=1

            else:
                if nums[i] >=0 and temp[k-1] < 0:
                    temp.append(nums[i])
                    i+=1
                elif nums[j] < 0 and temp[k-1] >= 0:
                    temp.append(nums[j])
                    j+=1
                else:
                    if nums[i] < 0:
                        i+=1
                    if nums[j] > 0:
                        j+=1
        k = len(temp)
        while k!=n and i < n:
            k = len(temp)
            if temp[k-1] < 0 and nums[i] >= 0:
                temp.append(nums[i])
                i+=1
            else:
                i+=1
        while k!=n and j < n:
            k = len(temp)
            if temp[k-1] >= 0 and nums[j] < 0:
                temp.append(nums[j])
                j+=1
            else:
                j+=1
        return temp

            

        