class Solution:
    def merg(self,arr, l, mid, r):
        i = l
        j = mid +1
        temp = []
        while i <= mid and j <= r:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i+=1
        while j <= r:
            temp.append(arr[j])
            j+=1
        count = 0
        while count < len(temp):
            arr[count + l] = temp[count]
            count +=1
        
        return arr
                
    def mergeSort(self, arr, l, r):
        if l >= r:
            return
        mid = (l+r)//2
        
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        return self.merg(arr, l, mid, r)
        