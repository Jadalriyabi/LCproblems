class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        #lets store a list of number logs and list of alp logs
        nums = list()
        alp = list()

        for entry in logs:
            idf, log = entry.split(' ', 1)
            
            if log[0].isdigit():
                nums.append(entry)
            else:
                alp.append(entry)
        
        #nums.sort()
        #idk this yet
        alp.sort(key = lambda x: (x.split(' ',1)[1], x.split(' ',1)[0]))
        return alp+nums
        