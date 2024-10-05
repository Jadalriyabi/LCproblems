class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # convert to lower case to normalize the paragrapgh
        paragraph = paragraph.lower()

        #remove punctuations in paragraph
        punctuation  = "!?.,/';"
        for char in punctuation :
            paragraph = paragraph.replace(char, ' ')

        #split paragraph into strings of chars stored in a array
        words = paragraph.split()
        
        #count words
        word_count = {}
        for word in words:
            if word in word_count: 
                word_count[word] += 1
            else:
                word_count[word] = 1  # Initialize count for new word

        
        #create a set of banned words
        banned_set = set(banned)
        
        #find most frequent non-banned word
        most_frequent_word = ""
        max_frequency = 0

        for word, count in word_count.items():
            if word not in banned_set and count > max_frequency:
                max_frequency = count
                most_frequent_word = word
        
        return most_frequent_word
    
    
