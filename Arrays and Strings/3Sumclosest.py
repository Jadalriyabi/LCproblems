class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Sort the nums
        
        #iterate through the array, fixing one element at a time
        
        #use two pointers to find the other elements that can add up to the target
        
        #update the closest sum whenever a new current sum is found
        
        #return the closest sum
        
        nums.sort()
        #closest_sum will store the closest sum we find to the target. We start with infinity so that any valid sum we find will replace it.
        closest_sum = float('inf')
        
        # This starts a loop from the first element of nums to the third-last element (since we're dealing with triplets).
        for i in range(len(nums) - 2):
            left= i + 1
            right = len(nums) -1
            
            while left < right:
                
                current_sum = nums[i] + nums[left] + nums[right]
                
                #Checks if the current sum is closer to the target than the previously stored closest_sum. If it is, update closest_sum
                if abs(current_sum -target) < abs(closest_sum -target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        return closest_sum