class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        #sort the intervals
        start = first index
        end = last index
        
        loop thru
            if( start <= x and x <= end and end < y):
                end = y
            if( start <= y and y <= end and x < start):
                start = x
            [0,4]
            if( x > start and y > end ):
                result.append([start,end])
                start = x
                end = y
            if(x < start and y < end):
                result.append([start,end])
                start = x
                end = y
        """
        if(len(intervals) == 0):
            return []
        orderedInt = sorted(intervals)
        start = orderedInt[0][0]
        end = orderedInt[0][1]
        result = []
        
        for i in range(1,len(orderedInt)):
            if( start <= orderedInt[i][0] and orderedInt[i][0] <= end and end < orderedInt[i][1]):
                end = orderedInt[i][1]
            if(start <= orderedInt[i][1] and orderedInt[i][1] <= end and start > orderedInt[i][0]):
                start = orderedInt[i][0]
            #if(start <= orderedInt[i][0] and orderedInt[i][1] < end):
            #    start = start
            #    end = end
            if(orderedInt[i][0] > end):
                result.append([start,end])
                start = orderedInt[i][0]
                end = orderedInt[i][1]
        
        result.append([start,end])
        return result
                
        
        
