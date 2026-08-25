class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        temp = []
        freq = {}
        for x in arr1:
            freq[x] = freq.get(x, 0) + 1
        for x in arr2:
            count = freq[x]
            for _ in range(count):
                temp.append(x)
            freq[x] = 0
        for i in sorted(freq):
            if freq[i] > 0:
                for _ in range(freq[i]):
                    temp.append(i)
        return temp
                
        