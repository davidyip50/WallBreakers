class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        
        find the number of keys
        
        if keys >= candies divie 2 = max = candies dive 2
        
        else:
            number of keys?

        [1,2,3,4,2,2]
        
        [1,1,1,2,2,2]
        [1,2,2,3]
        
        
        [1,2,3,4,4,6]
        
        """
        candyDict = {}
        stop = len(candies) / 2
        
        sister = []
        brother = []
        
        for i in candies:
            if(i in candyDict):
                candyDict[i] += 1
            else:
                candyDict[i] = 1
        
        if(len(candyDict) >= stop):
            return stop
        else:
            return len(candyDict)
            
        
