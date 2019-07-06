class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseDict = {"a":".-",
                     "b":"-...",
                     "c":"-.-.",
                     "d":"-..",
                     "e":".",
                     "f":"..-.",
                     "g":"--.",
                     "h":"....",
                     "i":"..",
                     "j":".---",
                     "k":"-.-",
                     "l":".-..",
                     "m":"--",
                     "n":"-.",
                     "o":"---",
                     "p":".--.",
                     "q":"--.-",
                     "r":".-.",
                     "s":"...",
                     "t":"-",
                     "u":"..-",
                     "v":"...-",
                     "w":".--",
                     "x":"-..-",
                     "y":"-.--",
                     "z":"--.."}
        
        currentWord = ""
        prevWord = ""
        checks = {}
        result = 1
        
        
        
        if(len(words) == 0):
            return 0
        
        
        for letters in words[0]:
            prevWord += morseDict[letters]

        for word in words:
            for letters in word:
                currentWord += morseDict[letters]
                
                
            if(currentWord not in checks):
                checks[currentWord] = 1
            prevWord = currentWord
            currentWord = ""
        return len(checks)
