class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        result = str.isupper(str(word))
        resultLow = str.islower(str(word))
        if(result == True):
            return True
        elif(resultLow == True):
            return True
        else:
            return str.isupper(str(word[0])) and str.islower(str(word[1:]))
