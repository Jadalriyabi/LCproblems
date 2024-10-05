class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
          #Step 1: create a roman numeral to integer map
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000,
        }

        # intiilize the reuslt which is our toal number at the end
        result = 0
       
        # Get the length of the Roman numeral string
        n = len(s)

        for i in range(n):
            # Check if the current Roman numeral is less than the next
            # i < n - 1 ensures that we're not at the last character in the string (to avoid index out of bounds errors when checking s[i + 1]).        
            # roman_map[s[i]] < roman_map[s[i + 1]] checks if the current Roman numeral is less than the next Roman numeral. This handles special cases like "IV" (4) or "IX" (9), where a smaller numeral comes before a larger one, indicating subtraction.
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                #Subtract the current numeral from total
                result -= roman_map[s[i]]
            else:
                result += roman_map[s[i]]
                
        return result

        