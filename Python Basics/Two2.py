# Given a list of non-negative integers, return a list of those numbers multiplied by 2, omitting any of the resulting numbers that end in 2.

# two2([1, 2, 3]) → [4, 6]
# two2([2, 6, 11]) → [4]
# two2([0]) → [0]

def two2(nums):
    
    result = []

    if not nums: 
        return result

    for num in nums:
        doubled = num * 2
        # Check if the last digit is not 2
        if doubled % 10 != 2:
            result.append(doubled)

    return result