class Solution(object):
    def isIsomorphic(self, s, t):
        n = len(s)
        freq = {}
        for i in range(n):
            if s[i] in freq and t[i] != freq[s[i]]:
                return False
            elif s[i] not in freq:
                if t[i] in freq.values():
                    return False
                else:
                    freq[s[i]] = freq.get(s[i],t[i])
        return True
  