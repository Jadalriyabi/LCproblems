class FileSystem(object):

    def __init__(self):
        #inialitze a dictionary with the paths adn thier respective values
        self.paths = {}

    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        #Checking if path is a empty strings, just a dash or if it exists in the Fileststem paths dictionary
        if len(path) == 0 or path == "/" or path in self.paths:
            return False

        #find the parent by splitting the path
        parent = path[:path.rfind('/')]

        # The parent must either be an empty string (for root-level paths) or must exist in self.paths
        if parent and parent not in self.paths:
            return False

        # Add the new path with its value to the dictionary
        self.paths[path] = value
        return True


    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        #This method checks if the requested path exists in the dictionary. If it does, it returns the associated value; otherwise, it returns -1.
        return self.paths.get(path, -1)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
