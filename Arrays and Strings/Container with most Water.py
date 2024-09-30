class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
#         #BRUTE FORCE
#         result = 0

#         for l in range(len(height)):
#             for r in range(l+1, len(height)):
#                 #the height can only go as high as the shortest wall
#                 area = (r - l) * min(height[l], height[r])
#                 result = max(result,area)

#         return result
         
        #O(N) solution
        result = 0 
        
        #Two pointers, one at the left and one at the end of the array
        left = 0
        right = len(height) - 1

        while left < right:
            #calaucteing area of the conatiner bound the min hieght or each wall
            area = (right - left) * min(height[left], height[right])
            result = max(area, result)
            
            #if the left wall is smaller then the right wall then we move to the next left wall
            if height[left] < height[right]:
                left += 1
            #if the left wall is bigger then the right wall then we decrement right wall, or if the are both equal we decemrnet the right wall. NOte that we could decremrnt the left wall in the case they are bothe equal
            else: 
                right -= 1
        return result