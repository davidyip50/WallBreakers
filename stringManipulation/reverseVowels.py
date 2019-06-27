class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelPostion = []
        result = []
        for i in range(len(s)):
            result.append(s[i])
            if(s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u"):
                vowelPostion.append(i)
            if(s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U"):
                vowelPostion.append(i)
                
        stop = int(len(vowelPostion)/2)
        length = len(vowelPostion) - 1
        temp = ""
        for i in range(stop):
            temp = result[vowelPostion[i]]
            result[vowelPostion[i]] = result[vowelPostion[length - i]]
            result[vowelPostion[length - i]] = temp
        
        return "".join(result)
