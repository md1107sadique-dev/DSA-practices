class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        left = 0
        right = len(matrix)-1
        for i in range(n):
            left = 0
            right = len(matrix) - 1
            while left <= right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left +=1
                right -=1
        