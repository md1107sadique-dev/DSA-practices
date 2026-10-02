class Solution(object):
    def frequencySort(self, s):
        if len(s) <= 1:
            return s
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        x = ""
        while freq:
            max_key = max(freq, key=freq.get)
            x += max_key*freq[max_key]
            del freq[max_key]
        return x


        