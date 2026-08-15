class Solution:
    def isPalindrome(self, s):
        l = 0
        r  = len(s)-1
        def rec(s,l,r):
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            return rec(s, l+1, r-1)
            
        return rec(s,l,r)