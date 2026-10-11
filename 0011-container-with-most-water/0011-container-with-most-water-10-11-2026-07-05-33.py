class Solution(object):
    def maxArea(self, height):
        if len(height) == 0:
            return 0
        left = 0
        right = len(height) - 1
        maxx = 0
        while left < right:
            h = right - left
            if height[left] < height[right]:
                mini = height[left]
            else:
                mini = height[right]
            cal = h * mini
            if cal > maxx:
                maxx = cal
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return maxx
        