class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        checks = {}
        result = 0
        
        for i in s:
            if(i in checks):
                checks[i] = -1
            else:
                checks[i] = i
        
        
        for i in range(len(s)):
            if(checks[s[i]] != -1):
                return i
        return -1
        
