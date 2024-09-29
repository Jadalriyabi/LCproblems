#Represents a directory in our file system.
class DirectoryNode:
    def __init__(self, name):
        self.name = name #The name of the directory.
        self.children = {} #A dictionary that holds the contents of the directory. The keys are the names of the files or directories inside it, and the values are the corresponding DirectoryNode or FileNode objects.

class FileNode:
    def __init__(self, name, content = ""):
        self.name = name #The name of the file.
        self.content = content #The content of the file as a string. Defaults to an empty string if not provided.


class FileSystem(object):

    def __init__(self):
        #When we create a FileSystem object, we initialize it with a root directory represented by a DirectoryNode with the name "/".
        #The root directory is the starting point of our file system, like the main folder on your computer.
        self.root = DirectoryNode("/")

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        # Split the path and traverse the file system to find the node.Calls the helper method _traverse(path) to find the node (file or directory) at the given path.
        node = self._traverse(path)
        if isinstance(node, FileNode):
            # If it's a file, return its name.
            return [node.name]
        else:
            # If it's a directory, return sorted list of its children names.
            return sorted(node.children.keys())

        
    #Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        # Split the path and traverse, creating directories as needed.
        self._traverse(path, create=True)
        
    #void addContentToFile(String filePath, String content)
    #If filePath does not exist, creates that file containing given content.
    #If filePath already exists, appends the given content to original content.
    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        # Traverse to the parent directory of the file.
        #Splits the file path into the parent directory path and the file name using the helper method _splitPath(filePath).
        parent_path, file_name = self._splitPath(filePath)
        #Navigates to the parent directory using _traverse(parent_path, create=True), creating it if it doesn't exist.
        parent_node = self._traverse(parent_path, create=True)
        
        #Checks if the file already exists in the parent directory's children:
        if file_name in parent_node.children:
            # If it does, appends the new content to the existing content.
            file_node = parent_node.children[file_name]
            file_node.content += content
        #If it doesn't, creates a new FileNode with the given content and adds it to the parent directory's children.
        else:
            # Create a new file node.
            parent_node.children[file_name] = FileNode(file_name, content)
        
    #Returns the content in the file at filePath.
    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        #Traverse to the node and return its content
        node = self._traverse(filePath)
        #check if node is a fileNode
        if isinstance(node, FileNode):
            return node.content
        else:
            raise ValueError("Path is a directory, not a file")

    #Navigates through the file system to find the node at the given path. Can also create directories along the way if needed.
    def _traverse(self, path, create=False):
        # Helper method to traverse the file system.
        # Splits the path into parts by separating on '/' and removes any empty strings (which can happen if there are leading or trailing slashes).
        path_parts = [part for part in path.split('/') if part]
        #Starts at the root directory.
        current = self.root
        
        #Iterates over each part in the path:
        for part in path_parts:
            #Checks if the part (directory or file name) exists in the current node's children.
            #If it doesn't exist:
            if part not in current.children:
                #If create is True, creates a new DirectoryNode and adds it to the current node's children.
                if create:
                    # Create a new directory node if it doesn't exist.
                    current.children[part] = DirectoryNode(part)
                else:
                    #If create is False, raises an error because the path doesn't exist
                    raise ValueError("Path does not exist.")
            #Moves to the next node in the path by setting current to the child node corresponding to the part.
            current = current.children[part]
        #After traversing all parts, returns the node at the end of the path.
        return current

        #Splits a full path into two parts: the parent directory path and the file or directory name at the end.
    def _splitPath(self, path):
    # Helper method to split the path into parent path and file/directory name.
    #Removes any trailing slashes from the path to avoid empty parts.
        if '/' not in path:
            return "/", path
        
        #Splits the path into parts by '/'.
        parts = path.rstrip('/').split('/')
        #The last part is considered the file or directory name (file_name).
        file_name = parts.pop()
        #The remaining parts are joined back together to form the parent path (parent_path).
        parent_path = '/' + '/'.join(parts)
        return parent_path, file_name
        #For example, /a/b/c/d becomes:
        #parent_path: /a/b/c
        #file_name: d




# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)