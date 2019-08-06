from collections import defaultdict
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        #create a map of all the occurs of the letter
        #when a new letter occurs add it to a string checks
        #go thru the map and sub tract every time you see the letter
        #when the letter hits zero take it off the checks
        
        
        maybe do something with intervals?
        """
        hit = defaultdict(list)
        points = []
        for i in range(len(S)):
            if(S[i] in hit):
                hit[S[i]][1] = i
            else:
                hit[S[i]].append(i)
                hit[S[i]].append(i)
        for key,val in hit.items():
            points.append(val)
        
        if(len(points) == 0):
            return 0
        sortPoints = sorted(points)
        start = sortPoints[0][0]
        end = sortPoints[0][1]
        distance = end - start
        currentPoints = [(start,end)]
        result = []
        result2 = []
        
        for i in range(1,len(sortPoints)):
            
            compareStart = sortPoints[i][0] 
            compareEnd = sortPoints[i][1]
            print(start,end)
            
            if((start <= compareStart and end >= compareStart) or (start <= compareEnd and end >= compareEnd)):
                if(compareStart < start):
                    start = compareStart
                #if it fits inside the interval and the end of the interval is bigger than the current 
                #end then update it because that means the parition should end there
                #ex: [16,19] [17,22] [20,20]
                # if the end interval is not update then 20,20 will not be include since the end will still be
                # [16,19]
                if(compareEnd > end):
                    end = compareEnd
                currentPoints.append((sortPoints[i][0],sortPoints[i][1]))
            else:
                result2.append(end - start + 1)
                result.append(currentPoints)
                start = sortPoints[i][0]
                end = sortPoints[i][1]
                distance = end - start
                currentPoints = [(start,end)]
        #print(result)
        result.append(currentPoints)
        result2.append(end - start + 1)

        print(result)
        return result2
        #return len(result)
        
