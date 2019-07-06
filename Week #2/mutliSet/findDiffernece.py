class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #cover empty string?
        checks = {}
        checks2 = {}
        for i in s:
            if(i in checks):
                checks[i] += 1
            else:
                checks[i] = 1
        for i in t:
            if(i in checks2):
                checks2[i] += 1
            else:
                checks2[i] = 1
        
        
        for i in t:
            if(i not in checks):
                return i
            if(i in checks and checks[i] != checks2[i]):
                return i
        
        
