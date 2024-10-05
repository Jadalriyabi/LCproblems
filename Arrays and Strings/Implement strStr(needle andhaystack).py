class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        left = 0  # Pointer for haystack
        right = 0  # Pointer for needle

        # Loop while both pointers are within the bounds of their respective strings
        while left < len(haystack) and right < len(needle):
            # Compare the characters at left (haystack) and right (needle)
            if haystack[left] == needle[right]:
                # Characters match, increment both pointers
                right += 1
                left += 1
            else:
                # Mismatch: move left pointer in haystack to next potential start point
                left = left - right + 1
                right = 0  # Reset right pointer (needle) to 0 to start checking again

            # If we've matched the entire `needle`, return the starting index
            if right == len(needle):
                return left - len(needle)

        # If we finish the loop and needle is not found, return -1
        return -1