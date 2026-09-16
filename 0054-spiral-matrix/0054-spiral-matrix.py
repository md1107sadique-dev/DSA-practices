class Solution(object):
    def spiralOrder(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        top = 0
        buttom = n-1
        left = 0
        right = m-1
        nums = []
        while left <= right and top <= buttom:
            # 1. left → right
            for i in range(left,right+1):
                nums.append(matrix[top][i])

            top += 1


            # 2. top → bottom
            for i in range(top,buttom+1):
                nums.append(matrix[i][right])

            right -= 1


            # 3. right → left
            if top <= buttom:
                for i in range(right, left - 1,-1):
                    nums.append(matrix[buttom][i])

                buttom -= 1

            # 4. bottom → top
            if left <= right:
                for i in range(buttom, top - 1, -1):
                    nums.append(matrix[i][left])

                left += 1
        return nums
                