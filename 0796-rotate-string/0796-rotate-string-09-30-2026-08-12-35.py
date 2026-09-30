class Solution(object):
    def rotateString(self, s, goal):
        n = len(s)
        if n != len(goal):
            return False
        # M-1
        # def rotate(s,goal):
        #     x = ""
        #     for i in range(n):
        #         if i == 0:
        #             z = s[:n-1]
        #             x = s[n-1] + z
        #         else:
        #             x = x[n-1] + x[:n-1]
        #         if x == goal:
        #             return True
        #     return False
        # x = rotate(s,goal)

        # M-2
        x = s + s
        if goal in x:
            return True
        return False  