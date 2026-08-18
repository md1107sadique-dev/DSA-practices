class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(0, n):
            minIndex = i
            for j in range(i+1,n):
                if arr[j] < arr[minIndex]:
                    minIndex = j
                
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr
        