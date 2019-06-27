class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        binary = ""
        rbinary = 0
        result = ""
        while(num != 0):
            binary += str(num % 2)
            num /= 2
            
        for i in binary:
            if(i == "0"):
                result += "1"
            else:
                result += "0"
                
        sLen = len(result) - 1 #5
        for i in range(sLen):
            if(result[i] == "1"):
                rbinary += int(math.pow(2,i))
        
        return rbinary
        
