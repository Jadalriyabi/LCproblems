# Write a function to return the sum of the numbers in the given array 'nums', except ignore sections of numbers starting with a 7 and extending to the next 8 (every 7 will be followed by at least one 8). 
# Return 0 for no numbers.

# sum78([1, 2, 2]) → 5
# sum78([1, 2, 2, 7, 99, 99, 8]) → 5
# sum78([1, 1, 7, 8, 2]) → 4

def sum78(nums):

    # Initialize sum to 0 and a flag to monitor if we are in a 7-8 section
    total_sum = 0
    in_section = False

    for num in nums:
        if num == 7:
            # If we find a 7, set the flag to True to start ignoring numbers
            in_section = True
        elif num == 8 and in_section:
            # If we find an 8 and we are in a section, end the section
            in_section = False
        elif not in_section:
            # If we are not in a section, add the number to the sum
            total_sum += num

    return total_sum
