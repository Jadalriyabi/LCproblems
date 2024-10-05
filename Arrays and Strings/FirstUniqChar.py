class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #dictionary to track characters
        charCount = {}

        # Step 2: Populate the character frequency dictionary
        for c in s:
            charCount[c] = 1 + charCount.get(c,0)

        
        #find the first non-reaprting character wihch would have a dic value of 1
        # Step 3: Find the first character with a frequency of 1
        for i in range(len(s)):
            if charCount[s[i]] == 1:
                return i
        
        # No unique character found
        return -1