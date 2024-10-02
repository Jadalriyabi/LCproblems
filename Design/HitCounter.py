#Should we worry about hits older then 300 seconds? can we get rid of them?

# Should we handle edge cases like no hits or a hit happeneing exactly at the 300-second mark

#can timestamps go beyond 5 minutes


#Brute force

#class HitCounter(object):

#    def __init__(self):
        #store timestamps of all hits
#        self.hits = []

#    def hit(self, timestamp):
#        """
#        :type timestamp: int
#        :rtype: None
#        """
        #Record the hit by adding the timestamp
#        self.hits.append(timestamp)
        

#   def getHits(self, timestamp):
#        """
#        :type timestamp: int
#        :rtype: int
#        """
         # Count the number of hits in the last 300 seconds

#        if not timestamp or timestamp < 0:
#            return 0

#        start_time = timestamp - 300

#        count = 0
#        for time in self.hits:
#            if time > start_time:
#                count += 1
#        return count

#Optimal Solution

class HitCounter:
    def __init__(self):
        #Instead of storing all timestamps, we can optimize by using a fixed-size array to store the number of hits for each second within the past 300 seconds.
        #We’ll maintain a sliding window of the last 300 seconds, so for each new hit or query, we only need to update a limited range of seconds.
        #Both arrays will be of size 300, since we only care about the last 300 seconds.
        self.hits = [] * 300
        self.times = [] * 300
    
    
    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        #Record the hit by adding the timestamp
        self.hits.append(timestamp)
        

    def getHits(self, timestamp):
        # Count the number of hits in the last 300 seconds
        start_time = timestamp - 300
        count = 0
        for t in self.hits:
            if t > start_time:
                count += 1
        return count
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


counter = HitCounter()
counter.hit(1)
counter.hit(2)

print(counter.hits[1])
print(counter.getHits(-1))

counter = HitCounter()
counter.hit(1)
counter.hit(1)
counter.hit(1)
print(counter.getHits(2))  # Expected output: 3 (all 3 hits happened at timestamp 1)


counter = HitCounter()
counter.hit(1)
counter.hit(2)
counter.hit(3)
print(counter.getHits(4))  # Expected output: 3 (all hits within last 300 seconds)