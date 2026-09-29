class Solution(object):
    def isIsomorphic(self, s, t):
        n = len(s)
        if n != len(t):
            return False
        freq = {}
        # M-1
        # for i in range(n):
        #     if s[i] in freq and t[i] != freq[s[i]]:
        #         return False
        #     elif s[i] not in freq:
        #         if t[i] in freq.values():
        #             return False
        #         else:
        #             freq[s[i]] = freq.get(s[i],t[i])

        # M-2
        treq = {}
        for i in range(n):
            if s[i] in freq:
                if freq[s[i]] != t[i]:
                    return False
            elif s[i] not in freq:
                freq[s[i]] = freq.get(s[i],t[i])
            if t[i] in treq:
                if treq[t[i]] != s[i]:
                    return False
            elif t[i] not in treq:
                treq[t[i]] = treq.get(t[i],s[i])
        return True
  