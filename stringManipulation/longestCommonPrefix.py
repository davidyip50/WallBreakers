class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs) == 1):
            return strs[0]
        infoDict = dict()
        
        for words in strs:
            key = ""
            for letters in words:
                key += letters
                if(key in infoDict):
                    infoDict[key] = infoDict[key] + 1
                else:
                    infoDict[key] = 0
            key = ""
        
        maxVal = 0
        maxLen = 0
        result = ""
        for key,val in infoDict.items():
            if(len(key) > maxLen and val >= maxVal and val != 0 and val == len(strs)-1):
                maxVal = val
                maxLen = len(key)
                result = key
        return result
                    
