class Solution(object):
    def maximumWealth(self, accounts):
        n = len(accounts)
        m = len(accounts[0])
        maxx = 0
        for i in range(n):
            summ  = 0
            for j in range(m):
                summ += accounts[i][j]
            if summ > maxx:
                maxx = summ
        return maxx