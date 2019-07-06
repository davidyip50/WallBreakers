class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        checksA = {}
        checksB = {}
        listA = A.split(" ")
        listB = B.split(" ")
        result = set()
        
        for i in listA:
            if(i in checksA):
                checksA[i] += 1
            else:
                checksA[i] = 1
            
        for i in listB:
            if(i in checksB):
                checksB[i] += 1
            else:
                checksB[i] = 1
        
        for i in listB:
            if(i not in checksA and checksB[i] == 1):
                result.add(i)
                
        for i in listA:
            if(i not in checksB and checksA[i] == 1):
                result.add(i)
        result2 = []
        
        for i in result:
            result2.append(i)
        return result
        
