class TextEditor(object):

    def __init__(self):
        # self.left will store characters to the left of the cursor.
        # We use a list to simulate a stack for efficient append and pop operations at the end.
        self.left_part = [] # Characters to the left of the cursor.
        # self.right will store characters to the right of the cursor.
        # We use deque for efficient insertions and deletions at both ends.
        self.right_part = deque() # Characters to the right of the cursor.
        
    #Appends text to where the cursor is. The cursor ends to the right of text.
    def addText(self, text):
        """
        :type text: str
        :rtype: None
        """
        #add text to the left of cursor
        for ch in text:
            #append each character to the left part []
            self.left_part.append(ch)

        
    #Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.
    def deleteText(self, k):
        """
        :type k: int
        :rtype: int
        """
        # Delete up to k characters to the left of the cursor.
        # Calculate the actual number of characters we can delete.
        delete_count = min(k, len(self.left_part)) # determine who many we can delete
        for _ in range(delete_count):
            self.left_part.pop() #remove characters from the left part

        #Returns the number of characters actually deleted.
        return delete_count # Return the number of characters actually deleted.
        
    #Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
    def cursorLeft(self, k):
        """
        :type k: int
        :rtype: str
        """
        # Move the cursor left by up to k positions.
        # Calculate how many positions we can actually move.
        move_count = min(k, len(self.left_part))# Cannot move beyond the start of the text.

        for _ in range(move_count):
            # Move characters from the left stack to the right deque.
            self.right_part.appendleft(self.left_part.pop())
        
        # Return the last 10 characters to the left of the cursor as a string.
        return ''.join(self.left_part[-10:])# Get up to 10 characters from the end of self.left.
        
    #Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
    def cursorRight(self, k):
        """
        :type k: int
        :rtype: str
        """
        #move the right cursor by k positions. # Calculate how many positions we can actually move.
        move_count = min(k, len(self.right_part))

        for _ in range(move_count):
            # Move characters from the right deque back to the left stack.
            self.left_part.append(self.right_part.popleft()) #move from right to left

        # Return the last 10 characters to the left of the cursor as a string.
        return ''.join(self.left_part[-10:])# Get up to 10 characters from the end of self.left.
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)