#clariftying questions:How is the cache organized?
#The cache uses a combination of a dictionary for fast access and a doubly linked list for managing the order of usage.

#What happens when the cache reaches its capacity?
#  When the capacity is reached, the least recently used (LRU) key is removed to make space for a new entry.

#How are recent accesses handled?
#Every time a key is accessed, it becomes the most recently used and is moved to the end of the doubly linked list.

#The Node class defines a structure to store the key and value, and pointers to the previous and next nodes in the doubly linked list.
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache(object):
    #The LRUCache manages the capacity, cache (hashmap), and the doubly linked list with two dummy nodes (left and right).
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity  # Store capacity
        self.cache = {}  # Hashmap to store key -> node

        # Left and right are dummy nodes to simplify insertions/removals
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])  # Move to the most recently used position
            self.insert(self.cache[key])
            return self.cache[key].val  # Return the value
        return -1  # Key not found
    
    #This method removes a node from the doubly linked list by connecting the node's previous node to its next node, effectively "skipping" the node to be removed.   
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        # Re-link previous and next nodes
        prev.next = nxt 
        nxt.prev = prev 
        
    #This method inserts a node at the most recently used position, just before the right dummy node.
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
         
        # Link the node between the previous last node and right
        prev.next = node
        nxt.prev = node
        
        node.next = nxt
        node.prev = prev
    #The put() method first checks if the key already exists. If it does, the existing node is removed and replaced with the new value. If the cache exceeds the capacity, the least recently used node (just after the left dummy node) is removed.
    def put(self, key, value): 
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])  # Remove the old node
    
        # Add the new key-value pair
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])  # Insert as most recently used

        # If the cache exceeds capacity, remove the least recently used node
        if len(self.cache) > self.cap:
            lru = self.left.next  # The node after left is the least recently used
            self.remove(lru)  # Remove it
            del self.cache[lru.key]  # Remove from the cache

            
            #Time Complexity: O(1) for both get() and put() because the operations are constant time due to the hashmap (dictionary) and doubly linked list.

            
            #Space Complexity: O(n) where n is the number of items in the cache, since we store up to n key-value pairs in the cache.
            
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)