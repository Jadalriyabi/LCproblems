class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Base case: If t is empty, return an empty string as there's nothing to search for
        if t == "":
            return ""
        
        # Dictionaries to store the character frequencies of t and the current window in s
        countT = {}
        window = {}

        # Count the frequency of each character in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # 'have' keeps track of how many characters in the current window satisfy the requirement of t
        have = 0
        # 'need' is the total number of unique characters in t that we need to match in the window
        need = len(countT)
        
        # 'result' will store the best (smallest) window's left and right indices
        # Start with [-1, -1] because we haven't found any valid window yet
        result = [-1, -1]
        # Initialize result_len to infinity since we want to minimize this length
        result_len = float("infinity")
        # 'left' pointer marks the start of the sliding window
        left = 0

        # Loop over each character in s with 'right' pointer expanding the window
        for right in range(len(s)):
            # Get the current character at the right boundary
            c = s[right]
            # Update the window with the current character count
            window[c] = 1 + window.get(c, 0)

            # If the current character exists in t and its frequency in the window matches countT
            if c in countT and window[c] == countT[c]:
                # Increase 'have' because we have matched one more character completely
                have += 1

            # When all characters from t are covered in the window, try to shrink the window
            while have == need:
                # Update the result if the current window is smaller than the previous best
                if (right - left) < result_len:
                    result = [left, right]
                    result_len = (right - left + 1)

                # Start shrinking the window from the left by removing s[left]
                window[s[left]] -= 1
                # If the removed character is in t and no longer satisfies the requirement
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    # Decrease 'have' since the window is no longer valid
                    have -= 1
                # Move the left pointer to reduce the window size
                left += 1

        # Extract the left and right boundaries of the smallest window found
        left, right = result
        # Return the substring if we found a valid window, otherwise return an empty string
        return s[left : right + 1] if result_len != float("infinity") else ""