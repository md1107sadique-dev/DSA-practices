class Solution:
    def findUnion(self, a, b):
        temp = []
        j = 0
        i = 0
        n = len(a)
        m = len(b)
        while i < n and j < m:
            k = len(temp)
            if a[i] <= b[j]:
                if k == 0 or temp[k-1] != a[i]:
                    temp.append(a[i])
                i+=1
            else:
                if k == 0 or temp[k-1] != b[j]:
                    temp.append(b[j])
                j+=1
        while i < n:
            k = len(temp)
            if k == 0 or temp[k-1] != a[i]:
                    temp.append(a[i])
            i+=1
                    
        while j < m:
            k = len(temp)
            if k == 0 or temp[k-1] != b[j]:
                temp.append(b[j])
            j+=1
        return temp