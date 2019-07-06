from collections import defaultdict
import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        checks = defaultdict(int)
        lowerStr = paragraph.lower()
        
        lowerStr = re.sub(r'[^\w\s]',' ',lowerStr)
        words = lowerStr.split(" ")
        
        for i in words:
            if(i not in banned and i in checks):
                checks[i] += 1
            if(i not in banned and i not in checks):
                checks[i] = 1
                
        maxResult = 0
        result = ""
        
        for key,value in checks.items():
            #print(key,value)
            if(key != "" and value > maxResult):
                maxResult = value
                result = key
        print(checks[result])
        return result
