class Solution:
    def thirdMax(self, nums):
        first = second = third = None

        for num in nums:

            # Duplicate ko skip karo
            if num == first or num == second or num == third:
                continue

            # First maximum
            if first is None or num > first:
                third = second
                second = first
                first = num

            # Second maximum
            elif second is None or num > second:
                third = second
                second = num

            # Third maximum
            elif third is None or num > third:
                third = num

        # Agar third maximum nahi mila
        if third is None:
            return first

        return third