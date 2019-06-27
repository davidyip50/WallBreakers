class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        AB -> 26 + 2
        BA -> 26 * 2 + 1
        ZY ->  26 * 26 + 25
        AAA -> 26 * 26 * 1 + 26 * 1 + 1
        """
        sLen = len(s) - 1
        result = 0
        multi = 1
        for i in range(sLen,-1, -1):
            if(s[i] == "A"):
                result += multi * 1 #1
            if(s[i] == "B"):
                result += multi * 2
            if(s[i] == "C"):
                result += multi * 3    
            if(s[i] == "D"):
                result += multi * 4
            if(s[i] == "E"):
                result += multi * 5
            if(s[i] == "F"):
                result += multi * 6
            if(s[i] == "G"):
                result += multi * 7
            if(s[i] == "H"):
                result += multi * 8
            if(s[i] == "I"):
                result += multi * 9
            if(s[i] == "J"):
                result += multi * 10
            if(s[i] == "K"):
                result += multi * 11
            if(s[i] == "L"):
                result += multi * 12
            if(s[i] == "M"):
                result += multi * 13
            if(s[i] =="N"):
                result += multi * 14
            if(s[i] =="O"):
                result += multi * 15
            if(s[i] =="P"):
                result += multi * 16
            if(s[i] =="Q"):
                result += multi * 17
            if(s[i] =="R"):
                result += multi * 18
            if(s[i] =="S"):
                result += multi * 19
            if(s[i] =="T"):
                result += multi * 20
            if(s[i] =="U"):
                result += multi * 21
            if(s[i] =="V"):
                result += multi * 22
            if(s[i] =="W"):
                result += multi * 23
            if(s[i] =="X"):
                result += multi * 24
            if(s[i] =="Y"):
                result += multi * 25
            if(s[i] =="Z"):
                result += multi * 26
            multi *= 26 #26
        return result
