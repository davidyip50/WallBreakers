import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        regex = re.compile('[^a-zA-Z0-9]')
        s = regex.sub("",s)
        
        for i in range(len(s)):
            if(str.upper(str(s[i])) != str.upper(str(s[-(i + 1)]))):
                return False
        return True
    """
        if(len(s) == 0 or len(s) == 1):
            return True
        else:
            if(str.upper(str(s[0])) == str.upper(str(s[-1]))):
                return self.isPalindrome(s[1:-1])
            else:
                return False
    """
