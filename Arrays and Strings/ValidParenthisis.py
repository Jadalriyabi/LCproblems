# Can the input string contain characters other than parentheses?

# Determines if the function should handle or ignore unexpected characters.
# What should the function return for an empty string?

# Clarifies if False or True is the expected behavior for an empty input.

class Solution(object):
    def isValid(self, s):
        """
        Checks if the input string `s` contains valid parentheses.

        :type s: str
        :rtype: bool
        """
        # Step 1: Handle the edge case where the input string is empty
        if not s: 
            return False  # Return False for an empty input string

        # Step 2: Initialize a stack to keep track of open parentheses
        stack = []

        # Step 3: Create a mapping for closing parentheses to their corresponding opening parentheses
        closing_parn_map = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        # Step 4: Iterate over each character in the input string
        for c in s:
            # Step 5: Check if the character is a closing parenthesis
            if c in closing_parn_map:
                # Step 5a: Ensure the stack is not empty and the top of the stack matches the corresponding opening parenthesis
                if stack and stack[-1] == closing_parn_map[c]:
                    # Step 5b: If they match, pop the top of the stack
                    stack.pop()
                else:
                    # Step 5c: If they don't match, the parentheses are not valid
                    return False
            else:
                # Step 6: If the character is an opening parenthesis, push it onto the stack
                stack.append(c)

        # Step 7: Return True if the stack is empty (all parentheses are matched), otherwise return False
        return not stack
    
# Time Complexity:

# The time complexity is O(N), where N is the length of the string s. Each character is processed once, and operations on the stack (push and pop) are O(1).
# Space Complexity:

# The space complexity is O(N) in the worst case, where N is the number of characters in s (if all are opening parentheses). The stack size can grow up to the length of the input string.






