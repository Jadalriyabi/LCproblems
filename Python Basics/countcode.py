# Given an input string, return the number of times that the string "code" appears anywhere in the string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(s):
    #initalize a counter
    count = 0
# Iterate through the string, checking for "co" + any char + "e" 
    for i in range(len(s) - 3): # Subtract 3 to avoid out-of-range errors
        if s[i:i+2] == "co" and s[i + 3] == "e":
            count += 1
    return count