class Solution(object):
    def romanToInt(self, s):
        latter = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        total = 0
        for i in range(n):
            if i < n-1 and latter[s[i]] < latter[s[i+1]]:
                total -= latter[s[i]]
            else:
                total += latter[s[i]]
        return total
        