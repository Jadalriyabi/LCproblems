class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # Split version strings by '.' to get individual version numbers
        #this splits both version strings (e.g., "1.0.1") into lists of individual version numbers using '.' as a delimiter.
        #Example:
        #If version1 = "1.0.1", v1 becomes ["1", "0", "1"].
        #If version2 = "1.0", v2 becomes ["1", "0"].
        v1 = version1.split('.')
        v2 = version2.split('.')

        # Find the longer of the two version lists to compare all parts
        max_len = max(len(v1), len(v2))

        # Compare each part of the version string (converted to int)
        for i in range(max_len):       
            # Get the current version part for version1 (if shorter, use 0 as default)
            # This code extracts the current part of each version (from v1 and v2) and converts it to an integer.
            # If the current index i is within the length of the version list (v1 or v2), it fetches that part and converts it to an integer using int().
            # If i exceeds the length of the version list, meaning one version is shorter, it defaults to 0.
            part1 = int(v1[i]) if i < len(v1) else 0 
            # Get the current version part for version2 (if shorter, use 0 as default)
            part2 = int(v2[i]) if i < len(v2) else 0
            
            # Compare current parts
            if part1 > part2:            
                  # version1 is greater
                return 1
                  # version2 is greater
            elif part2 > part1:
                return -1

        # If no difference is found after comparing all parts, return 0 (versions are equal)
        return 0