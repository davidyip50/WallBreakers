class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        sort the points distance in acs
            :allows the
        need to find the max number of ballons with the same x
            6       6       5       5
        [[10,16], [2,8], [1,6], [7,12]]
        [[1,6], [2,8]] ,[7,12], [10,16]]
        start = 1
        end = 6
        1 - 6 = 5
        2 - 6 = 4
        distance = 5
        8 - 2 = 6
        8 - 7 = 1
        8 - 10 = -2
        for i in points[1:-1]:
            copy[0] += distance
            copy[1] -= distance
            if(start <= copy[0] and end >= copy[0] or start <= copy[1] and end >= copy[1]):
                index += 1
            else:
                result += 1
                min = i[0]
                max = i[1]
                distance = i[1] - i[0]
        
        1) 
        
        Means I would need to loop through the groups to see if it fits
        hash of group list of grouped tuples using the first index as a req to get in
        #order by space covered
        #if fits requirement of put into the group
        #else
            make a new group
            
        what did we learn?
            check for things that will break the greedy alg
            remember to list all possible and all choices the alg needs to make
            
        """
        
        if(len(points) == 0):
            return 0
        sortPoints = sorted(points)
        start = sortPoints[0][0]
        end = sortPoints[0][1]
        distance = end - start
        currentPoints = [(start,end)]
        result = []
        
        for i in range(1,len(sortPoints)):
            
            compareStart = sortPoints[i][0] 
            compareEnd = sortPoints[i][1]
            print(start,end)
            
            if((start <= compareStart and end >= compareStart) or (start <= compareEnd and end >= compareEnd)):
                #making the window smaller if the interval match because
                #we need to restrict what is in every interval
                #ex: [1,10] [6,7] [8,12]
                #if the window doesnt not get updated I.E. it always stays 1,10
                # then the result will only have one group
                #if the window is updated to [6,7]
                #two groups will form
                if(compareStart > start):
                    start = compareStart
                if(compareEnd < end):
                    end = compareEnd
                currentPoints.append((sortPoints[i][0],sortPoints[i][1]))
            else:
                result.append(currentPoints)
                start = sortPoints[i][0]
                end = sortPoints[i][1]
                distance = end - start
                currentPoints = [(start,end)]
        #print(result)
        result.append(currentPoints)
        print(result)
        return len(result)
