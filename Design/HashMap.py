class MyHashMap(object):

    def __init__(self):
        #the size is chosen based on an assumption that the keys will be within the range of 0 to 1,000,000.
        self.data = [None] * 1000001

    def put(self, key, value):a
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #The put method allows you to store a key-value pair. The key is treated as an index in the list self.data, and the value is stored at that index.
        #This method works like this:
        #You pass a key and a value.
        #The method directly sets self.data[key] = value, storing the value at the index equal to the key.
        self.data[key] = value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #The get method retrieves the value associated with a given key. It checks if there is a value stored at self.data[key].
        #If the value is None (i.e., the key is not present), it returns -1 to indicate that the key does not exist. Otherwise, it returns the value stored at that key.
        val = self.data[key]
        return val if val != None else -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        #The remove method deletes the value associated with the given key by setting self.data[key] = None.
        #This simulates the removal of the key by resetting its value to None.
        self.data[key] = None
        


# Instantiating MyHashMap object
obj = MyHashMap()

# Adding a key-value pair
obj.put(10, 50)  # Stores value 50 at key 10

# Retrieving the value associated with a key
print(obj.get(10))  # Outputs 50

# Removing the value associated with a key
obj.remove(10)

# Trying to retrieve the value again (after removal)
print(obj.get(10))  # Outputs -1 because key 10 has been removed
