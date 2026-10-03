class Solution(object):
    def maxDepth(self, s):
        maxi = 0
        som = 0
        for ch in s:
            if ch == "(":
                som += 1 
                if som > maxi:
                    maxi = som
            elif ch == ")":
                som -= 1
        return maxi
        