class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix) - 1

        while left < right:
            #we want to shift one square at at time
            for i in range(right - left):
                top, bottom = left, right

                #save the topleft value, our temp value. The 'i' shift will m,ove the index one position to the right
                topLeft = matrix[top][left + i]

                #move bottom left into top left.
                matrix[top][left + i] = matrix[bottom - i][left] # move up the matrix by pne

                #move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i] #move left in the matix

                #move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right] # move down in the matrix

                #move top left into top right
                matrix[top + i][right] = topLeft
            
            right -= 1
            left += 1