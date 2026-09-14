class Solution(object):
    def checkZeroOnes(self, s):
        n = len(s)
        maxx = 0
        smax = 0
        count = 0
        scount = 0
        for i in range(n):
            if s[i] == "1":
                count+=1
                scount = 0
                if count > maxx:
                    maxx = count
            if s[i] == "0":
                count = 0
                scount +=1
                if scount > smax:
                    smax = scount
        if maxx > smax:
            return True
        else:
            return False
        