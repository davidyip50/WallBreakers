class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        sLen = len(s) - 1 #5
        sEnd = len(s)/2 #2
        temp = "" #a
        #Hannah
        #hannaH
        for i in range(sEnd):#2
            temp = s[i] 
            s[i] = s[sLen - i] 
            s[sLen - i] = temp
        
