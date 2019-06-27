class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binaryN = ""
        rBinaryN = ""
        position = []
        
        while(N !=0):
            binaryN += str(int(N % 2))
            N = int(N/2)
        
        lenN = len(binaryN) - 1
        for i in range(lenN,-1,-1):
            rBinaryN += binaryN[i]
        
        for i in range(len(binaryN)):
            if(rBinaryN[i] == "1"):
                position.append(i)
                
        maxdiff = 0
        if(len(position) == 0 or len(position) == 1):
            return maxdiff
        
        for i in range(len(position)):
            if(i + 1 <= len(position) - 1 and position[i+1] - position[i] > maxdiff):
                maxdiff = position[i+1] - position[i]
        return maxdiff
            
