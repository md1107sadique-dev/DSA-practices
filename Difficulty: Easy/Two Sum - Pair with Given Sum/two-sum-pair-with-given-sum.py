class Solution:
    def twoSum(self, arr, target):

        seen = set()

        for num in arr:

            needed = target - num

            if needed in seen:
                return True

            seen.add(num)

        return False