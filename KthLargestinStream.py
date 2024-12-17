class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # O( m * n log (n) ) time complexity sorting algo, where m is the number of calls made to add() and n is the current size of array
        # O(1) or O(n) depending on the sorting algo
        #self.k = k
        #self.arr = nums

        self.minHeap, self.k = nums, k  # Store the input list as a min-heap and the value of k
        heapq.heapify(self.minHeap)     # Convert the input list into a min-heap
        
        # Ensure the heap contains only 'k' elements (trim excess elements)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  # Remove the smallest element (root of the heap)

    def add(self, val: int) -> int:     
        #self.arr.append(val)
        #self.arr.sort()
        #return self.arr[len(self.arr) - self.k]   
        heapq.heappush(self.minHeap, val)  # Add the new value to the heap
    
        # If the heap size exceeds k, remove the smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]  # Return the k-th largest element (smallest in the min-heap)
