class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binaryX = ""
        binaryY = ""
        while(x != 0):
            binaryX += str( int(x % 2))
            x = int(x / 2)

        while(y != 0):
            binaryY += str( int(y % 2))
            y = int( y / 2)

        #binaryX = 1
        #binaryY = 001
        #2
        compare = [binaryX,binaryY]
        maxLen = len(max(compare,key=len)) - 1


        #0
        lenX = len(binaryX) - 1
        #2
        lenY = len(binaryY) - 1

        for i in range(maxLen + 1):
            if(lenX < i):
                binaryX += "0"
            if(lenY < i):
                binaryY += "0"

        counter = 0
        for i in range(maxLen + 1):
            if(binaryX[i] != binaryY[i]):
                counter +=1 
        return counter
            
            
                
