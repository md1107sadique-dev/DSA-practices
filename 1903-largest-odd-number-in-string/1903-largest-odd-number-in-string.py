# class Solution(object):
#     def largestOddNumber(self, num):
#         res = ""
#         count = 0
#         for i in range(len(num)-1,-1,-1):
#             if int(num[i]) % 2 == 0:
#                 count += 1
#             else:
#                 break
#         x = len(num) - count
#         if x == 0:
#             return ""
#         else:
#             z = num[0:x]
#             return z

# m-2
class Solution(object):
    def largestOddNumber(self, num):
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]

        return ""