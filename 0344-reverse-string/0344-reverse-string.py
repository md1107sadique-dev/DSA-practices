class Solution(object):
    def reverseString(self, s):
        l = 0
        r = len(s)-1
        def rec(s, l,r):
            if l >= r:
                return
            s[l], s[r] = s[r], s[l]
            return rec(s,l+1,r-1)
        return rec(s,l,r) 
        