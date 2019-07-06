class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        patternDict = {}
        strList = str.split(" ")
        lenStr = len(strList)
        usedWord = set()
        if(len(pattern) != lenStr):
            return False
        for i in range(len(pattern)):
            if(pattern[i] in patternDict and patternDict[pattern[i]] != strList[i]):
                return False
            if(i < lenStr and pattern[i] not in patternDict):
                if(strList[i] in usedWord):
                    return False
                patternDict[pattern[i]] = strList[i]
                usedWord.add(strList[i])
        return True
                
        
