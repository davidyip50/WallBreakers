class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        #sort both arraies in acs order
        #allows me to give the cookie of the to the smallest greed first
        #once the cookie is give take it out of the array
         for children in range(len(sortG)):
            for snacks in range(len(sortS)):
                if(sortS[snacks] >= sortG[children]):
                    result += 1
                    sortS[snacks] = -1
                    break
        """
        sortG = sorted(g)
        sortS = sorted(s)
        lenG = len(g)
        start = 0
        result = 0
        
        for snacks in range(len(sortS)):
            if( start < lenG and sortS[snacks] >= sortG[start]):
                result += 1
                start += 1
        return result
                
        
