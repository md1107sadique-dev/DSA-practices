class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        # top = 0
        # bottom = m-1
        for i in range(m):
            low = 0
            high = n - 1 
            while low <= high:
                mid1 = (low + high)//2
                if matrix[mid1][i] == target:
                    return True
                elif matrix[mid1][i] > target:
                    high = mid1 - 1
                else:
                    low = mid1 + 1

        return False
                
                
        