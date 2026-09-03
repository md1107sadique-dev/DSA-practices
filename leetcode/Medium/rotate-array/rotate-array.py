class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        if n == 0:
            return 
        k %= n
        if k == 0:
            return

        # m-1(Brute force)
        # for i in range(1, k+1):
        #     temp = nums[n-1]
        #     for j in range(n-2,-1,-1):
        #         nums[j+1] = nums[j]
        #     nums[0] = temp

        # m-2(Optimal solution)
        def reverse(nums, l, r):
            if r <= l:
                return
            i = l
            j = r
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                i += 1
            
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)