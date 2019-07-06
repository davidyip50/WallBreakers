class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        data = str(n)
        result = 0
        counter = {}
        
        for i in data:
            result += int(math.pow(int(i),2))
        counter[result] = 1

        while(result != 1):
            data = str(result)
            result = 0
            for i in data:
                result += int(math.pow(int(i),2))
            
            if(result in counter):
                return False
            else:
                counter[result] = 1
        
        #1
        #1 + 0 = [3,1]
        #1 + 0 + 0 = [6,8]
        #1 + 0 + 0 + 0 = [30,10],[26,18]
        #1 + 0 + 0 + 0 + ...[28,96]
        # [8,2] = 68
        #happy numbers: 19, 109, 1009, 1900,... 8200
        return True
        
