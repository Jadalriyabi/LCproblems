# Write a function to round an int value up to the next multiple of 10 if its rightmost digit is 5 or more. 
# So 15 rounds up to 20, and 6 rounds up to 10. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
# Given 3 ints, a b c, return the sum of their rounded values.

# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10

#The round10 function checks the rightmost digit of the number. If it's 5 or more, the number is rounded up to the next multiple of 10. Otherwise, it rounds down to the previous multiple of 10.
def round10(n):
    #if rightmost digit is greater then 5 then we return 20
    if n % 10 >= 5:
        return ((n // 10) + 1) * 10
        
    else:
        return (n // 10) * 10

def round_sum(a, b, c):

   # Round each number and return the sum
  return round10(a) + round10(b) + round10(c)


# Test cases
print(round_sum(16, 17, 18))  # Output: 60
print(round_sum(12, 13, 14))  # Output: 30
print(round_sum(6, 4, 4))     # Output: 10