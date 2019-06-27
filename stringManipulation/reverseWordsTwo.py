class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = s.split(" ")
        result = []
        temp = ""
        for i in sList:
            sLen = len(i) - 1
            newStr = ""
            for letters in range(sLen,-1,-1):
                newStr += i[letters]
            result.append(newStr)
        return " ".join(result)
