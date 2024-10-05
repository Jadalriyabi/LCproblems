class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
         # Sort the nums list to make it easier to traverse and avoid duplicates
        nums.sort()
        
        # Use a set to store unique triplets
        nums_set = set()
        
        # Traverse the list, fixing the left element and using two pointers
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            
            # Traverse the list with two pointers
            while j < k:
                # Calculate the current sum
                current_sum = nums[i] + nums[j] + nums[k]
                
                if current_sum == 0:
                    # Add the triplet to the set to avoid duplicates
                    nums_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif current_sum < 0:
                    j += 1
                else:
                    k -= 1
        return nums_set
        
        
        
#         target = 0
#         nums.sort()
#         s = set()
#         output = []
#         for i in range(len(nums)):
#             j = i + 1
#             k = len(nums) - 1
#             while j < k:
#                 sum = nums[i] + nums[j] + nums[k]
#                 if sum == target:
#                     s.add((nums[i], nums[j], nums[k]))
#                     j += 1
#                     k -= 1
#                 elif sum < target:
#                     j += 1
#                 else:
#                     k -= 1
#         output = list(s)
#         return output
        