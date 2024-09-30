class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        possibile_nums = '0123456789'
        result = ''

        for char in s:
            #checking for leading whitespace in the begininig of the string
            if char == ' ' and len(result) == 0:
                continue
            #checking if char is not a white space and the first spot is postionve or negative sign
            if char != ' ' and (char in '-+' or char in possibile_nums) and len(result) == 0:
                result += char
            elif char in possibile_nums:
                result += char
            #if its not all these cases then break out of the loop
            else:
                break
        
        #checking for our result if its valid
        if result == '' or result in '-+':
            return 0
        else:
            if int(result) < -(2**31):
                return -(2**31)
            elif int(result) > (2**31 - 1):
                return (2**31 - 1)
            else:
                return int(result)

            
        
        