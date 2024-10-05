class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * (len(nums))

        #prefix for the first element
        prefix = 1
        #create prefix array
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        #postfix for last element
        postfix = 1
        #multiypy each prefix by the postfix to the the correct num in nums[i]
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result