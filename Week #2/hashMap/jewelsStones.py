class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        jewels = {}
        
        for i in J:
            jewels[i] = 1
                
        result = 0
        for i in S:
            if(i in jewels):
                result += 1
        return result
        
