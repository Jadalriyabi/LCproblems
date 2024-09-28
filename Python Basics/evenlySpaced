def evenlySpaced(a, b, c):
    # Sort the three numbers to identify small, medium, and large
    nums = sorted([a, b, c])
    
    # Check if the difference between small and medium is the same as medium and large
    return (nums[1] - nums[0]) == (nums[2] - nums[1])

# Test cases
print(evenlySpaced(2, 4, 6))  # True
print(evenlySpaced(4, 6, 2))  # True
print(evenlySpaced(4, 6, 3))  # False
