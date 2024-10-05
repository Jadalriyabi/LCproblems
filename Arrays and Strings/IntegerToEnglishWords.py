class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 1. Define mappings for single digits, teens, tens, and thousands.
        # 2. Create a helper function to handle numbers below 1000.
        # 3. Process each 3-digit segment of the number using the helper.
        # 4. Construct the final English words representation by concatenating the segment representations with appropriate thousand separators.
        
        #base case
        if num == 0: return "Zero"
        
        #define mapping
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def handle_number(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            #What it does: If n is less than 100, it finds the word for the tens place using tens[n // 10] and recursively calls helper(n % 10) for the ones place. so ex: 42 (42//10 == 4) and 42 %10 is 2
            elif n <100:
                return tens[n // 10] + " " + handle_number(n % 10)
            else:
                return below_20[n // 100] + " Hundred " + handle_number(n %  100)
            
        # Initializes an empty string result to build the final word representation.
        result = ""
        
        #Loops through the thousands list with index i to handle groups of three digits (units like "Thousand", "Million", etc.).
        #Reason: This loop processes each group of three digits in the numbe
        for i, unit in enumerate(thousands):
            # For each group of three digits, it calls helper to get the word representation and appends the corresponding unit from thousands.
            #Reason: If the current group of three digits is not zero, it processes that part and adds it to result.
            if num % 1000 != 0:
                result = handle_number(num % 1000) + unit + " " + result
            #Reduces the number by dividing it by 1000, essentially moving to the next group of three digits.
            num //= 1000
            
        #srips the reuslt with anyy tailing spaces
        return result.strip()
    
    
    