class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        countDictS = {}
        countDictT = {}
        if(len(s) != len(t)):
            return False
        for i in range(len(s)):
            if(s[i] in countDictS):
                countDictS[s[i]] += 1
            else:
                countDictS[s[i]] = 1
                
        for i in range(len(t)):
            if(t[i] in countDictT):
                countDictT[t[i]] += 1
            else:
                countDictT[t[i]] = 1
                
        for key,value in countDictT.items():
            if(key not in countDictS):
                return False
            if(value != countDictS[key]):
                return False
        return True
                
