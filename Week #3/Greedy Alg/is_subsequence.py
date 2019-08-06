from collections import defaultdict
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        brute force:
        
        does not account for position
        add var for position
            for t
                if t not in s:
                    return false
                if last found < current found:
                    return false
            return true
            
        find the position of letters in t
        if position same as s then return true
        else
            return false
        
        checks = defaultdict(int)
        compare = ""
        
        for i in s:
            checks[i] += 1
        
        for i in t:
            if(i in checks and checks[i] >= 1):
                compare += i
        return compare == s
        does not work because
        s = abc
        t = bahbgdc
        this is still true
        
        make a loop through t
            find first
            then second then third
        """
        start = 0
        match = 0
        lenSub = len(s)
        for i in t:
            if(start < lenSub and i == s[start]):
                start += 1
                match += 1
        return match == lenSub
        
            
            
        
