from collections import defaultdict
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        for letters in range(len(s)):
            spots = checks[s[letters]]
            for i in range(len(spots)):
                if(len(compareWord) != len(t)):
                    compareWord += t[letters]
        
        checks = defaultdict(list)#{e:[0],g[1,2]}
        indexT = {}
        compareWord = {}
        useLetters = set()
        for i in range(len(s)):
            checks[s[i]].append(i)
            
        for i in range(len(t)):
            indexT[i] = t[i]
            
        for letters in range(len(s)):
            spots = checks[s[letters]]
            for i in range(len(spots)):
                if(t[letters] not in useLetters):
                    compareWord[spots[i]] = t[letters]
            useLetters.add(t[letters])
        
        if(len(compareWord) != len(indexT)):
            return False
        
        for key in compareWord:
            if(compareWord[key] != indexT[key]):
                return False
        return True
    """
        
        mapping = {}
        compareWord = ""
        useLetters = set()

        
        for i in range(len(s)):
            if(s[i] not in mapping and t[i] not in useLetters):
                mapping[s[i]] = t[i]
                useLetters.add(t[i])
        
        for i in range(len(s)):
            if(s[i] in mapping):
                compareWord += mapping[s[i]]
            else:
                compareWord += s[i]
        return compareWord == t
        
