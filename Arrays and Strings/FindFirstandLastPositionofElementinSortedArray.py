class Solution(object):
    def searchRange(self, nums, target):
        # Helper function to find the first occurrence of the target
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    # Move to the left to find the first position
                    right = mid - 1
            # After the loop, left is the first occurrence if it's in bounds and equals target
            if left < len(nums) and nums[left] == target:
                return left
            return -1

        # Helper function to find the last occurrence of the target
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    # Move to the right to find the last position
                    left = mid + 1
            # After the loop, right is the last occurrence if it's in bounds and equals target
            if right >= 0 and nums[right] == target:
                return right
            return -1

        # Find the first and last positions
        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last] if first != -1 else [-1, -1]

    
#to avoid repeated code i could just create a binaery serach dfuniont and just call it to find first and last intead of writing two functions