class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #Step 1: list roman numeral values and their symbols
        roman_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), 
            (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'), 
            (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'), 
            (1, 'I')
        ]

        # Step 2: initalizing the strong to store our reuslt whihc we will append the correct value one by one
        result = ""

        for val, symbol in roman_symbols:
            #lets loop through the symbols starting from largest to smallest so we can get the right symbols in our string
            while num >= val:
                result += symbol
                num -= val
       
        return result