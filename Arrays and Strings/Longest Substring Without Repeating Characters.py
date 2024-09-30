class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
       # ans = {}

      #  for c in s:
      #      if c in ans:
      #          ans[c] += 1
     #       else:
        #        ans[c] = 1
      #  return max(ans, key = ans.get)
       
        # Initialize an empty set to store unique characters in the current window
        # Sets are ideal here because they automatically ensure there are no duplicates
        charSet = set()

        # 'left' pointer starts at the beginning of the string (left end of the sliding window)
        left = 0

        # 'result' will store the length of the longest substring without repeating characters
        result = 0

        # Iterate through the string with the 'right' pointer (right end of the sliding window)
        for right in range(len(s)):
            
            #while the character (could be multiple) at 'right' is already in the set, it's a duplicate
            while s[right] in charSet:
                # Remove the character at 'left' from the set to shrink the window
                charSet.remove(s[left])
                # Move the 'left' pointer to the right by one to exclude the duplicate
                left += 1
            
            # Add the current character at 'right' to the set, since it's unique now
            charSet.add(s[right])

            # Update the result with the maximum length of the substring seen so far
            # (right - left + 1) is the current window size
            result = max(result, right - left + 1)

        # After the loop, return the length of the longest substring found
        return result 

        # Time complexity: O(n) because we traverse the string once with two pointers
        # Space complexity: O(n) because the set stores up to n unique characters
        
        