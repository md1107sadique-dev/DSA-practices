class Solution(object):
    def threeSum(self, nums):
        arr = []
        n = len(nums)
        nums.sort()
        # Brute force(1)
        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #         for z in range(j+1, n):
        #             target = nums[i]+nums[j]+nums[z]
        #             if target == 0:
        #                 triplate = [nums[i],nums[j],nums[z]]
        #                 if triplate not in arr:
        #                     arr.append(triplate)

        # brute force(2)
        # for i in range(n-2):
        #     j = i + 1
        #     z = j + 1
        #     while j < n-1:
        #         target = nums[i]+nums[j]+nums[z]
        #         if target == 0:
        #             triplate = [nums[i],nums[j],nums[z]]
        #             if triplate not in arr:
        #                 arr.append(triplate)
        #         z += 1
        #         if z == n:
        #             j+=1
        #             z = j +1
        
        # Optimal
        for i in range(n-2):
            j = i + 1
            z = n - 1
            while j < z:
                target = nums[i]+nums[j]+nums[z]
                if target == 0:
                    triplate = [nums[i],nums[j],nums[z]]
                    if triplate not in arr:
                        arr.append(triplate)
                    j += 1
                    z -= 1
                elif target < 0:
                    j +=1
                else:
                    z -=1
                # if j == z:
                #     j+=1
                #     z = n-1

        return arr
            

        