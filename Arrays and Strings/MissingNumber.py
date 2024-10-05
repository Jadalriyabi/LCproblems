class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #creating a set whihc is all the unique nums in this list of ints
        numSet = set(nums)
        
         # Check for the missing number in the range from 0 to n (inclusive)
        for i in range(len(nums) + 1):
            if i not in numSet:  # If i is not in the set, it means it's the missing number
                return i