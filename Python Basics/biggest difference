# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 

# biggest_diff([10, 3, 5, 6]) → 7
# biggest_diff([7, 2, 10, 9]) → 8
# biggest_diff([2, 10, 7, 2]) → 8

def biggest_diff(nums):

    # Check if the list is not empty and has more than one element
    if nums and len(nums) > 0:
        # Find the maximum and minimum values in the list
        max_val = max(nums)
        min_val = min(nums)
        # Calculate the difference between the maximum and minimum values
        return max_val - min_val
    else:
        return 0  # Return 0 if the list is empty or not provided

def biggest_diff(nums):
    #checking if array is empty or not
    if not nums: return 0

    # Initialize both largest and smallest to the first element of the list
    minimum = nums[0]
    maximum = nums[0]

    #finding or max and min
    for num in nums:
        #if current num is greater then max then update max
        if num > maximum:
            maximum = num
        # if current num is less then min then update min
        if num < minimum:
            minimum = num

    #calculate the difference between the max and min to find the biggest difference
    biggest_difference = maximum - minimum

    #return biggest difference
    return biggest_difference
