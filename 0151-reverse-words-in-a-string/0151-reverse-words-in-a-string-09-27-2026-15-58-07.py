class Solution(object):
    def reverseWords(self, s):
        result = ""
        temp = []
        res = ""
        for ch in s:
            if ch !=" ":
                res +=  ch
            elif res:
                temp.append(res)
                res = ""
        if res:
            temp.append(res)
        
        for i in range(len(temp) - 1, -1, -1):
            result += temp[i]

            if i != 0:
                result += " "
        
        return result
