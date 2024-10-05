# Are the input strings guaranteed to be non-empty?

# Confirm whether the function should handle empty strings and how they should be treated.
# Can the input list contain duplicate strings?

# Clarify if the function should handle duplicate strings in the input list and if duplicates should be reflected in the output.
# What is the expected output format if there are no anagrams?

# Ensure that the interviewer is aware of what should be returned if no anagrams are present

class Solution(object):
    def groupAnagrams(self, strs):
        """
        Groups a list of strings into lists of anagrams.
        
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # Step 1: Create a dictionary to hold groups of anagrams.
        # The keys will be sorted strings, and the values will be lists of original strings that are anagrams.
        grouped = {}

        # Step 2: Iterate through each string in the input list.
        for word in strs:
            # Step 3: Sort the characters of the string.
            # Sorting transforms the string into a canonical form that is the same for all anagrams.
            sorted_word = ''.join(sorted(word))
            
            # Step 4: Check if the sorted string is already a key in the dictionary.
            if sorted_word in grouped:
                # If it is, append the original word to the existing list.
                grouped[sorted_word].append(word)
            else:
                # If it is not, create a new entry in the dictionary with the sorted string as the key and
                # initialize the list with the original word.
                grouped[sorted_word] = [word]
        
        # Step 5: Return the values of the dictionary as a list of lists.
        # Each list corresponds to a group of anagrams.
        return list(grouped.values())

    
#     Time Complexity:

# Sorting each string takes O(k log k) time, where k is the length of the string. Since there are n strings, the overall time complexity is O(n * k log k).
# Space Complexity:

# The space complexity is O(n * k) for storing the strings in the dictionary and the resulting output list.