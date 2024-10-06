# Return True if the string "cat" and "dog" appear the same number of times in the given string.

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(s):
    #checking for empty string
    if not s: 
        return False

    #count how many times dog and cat are in the string
    count_dog = s.count("dog")
    count_cat = s.count("cat")

    # Return True if the counts are the same, otherwise False
    return count_cat == count_dog

def cat_dog(s):
    #checking for empty string
    if not s: 
        return False

    count_dog = 0
    count_cat = 0

    for i in range(len(s) - 2): # len(s) - 2 because we are checking 3 characters at a time
        if s[i:i+3] == "cat":
            count_cat += 1
        elif s[i:i+3] == "dog":
            count_dog += 1

    # Return True if the counts are the same, otherwise False
    return count_cat == count_dog    
