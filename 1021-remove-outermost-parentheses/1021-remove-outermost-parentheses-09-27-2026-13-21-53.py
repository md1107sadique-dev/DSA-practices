class Solution(object):
    def removeOuterParentheses(self, s):
        count = 0
        result = ""
        for i in range(len(s)):
            if s[i] == "(" and count == 0:
                    count += 1 

            elif s[i] == "(":
                count += 1
                result += s[i]
            else:
                count -= 1
                if s[i] == ")" and count == 0:
                    continue
                result += s[i] 
        return result
        