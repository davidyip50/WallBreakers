import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        
        returnResult = []
        checks2 = collections.Counter(p)
        lenP = len(p)
        if (len(s) == 0):
            return []
        
        for i in range(len(s) - len(p) + 1):
            checks3 = collections.Counter(s[i:i + len(p)])
            result = checks3 - checks2
            if(len(result) == 0):
                returnResult.append(i)
        return returnResult
        if(s[i] in compare):
                begin = i
                checks[s[i]] = 1
            if(s[i] not in compare):
                checks = {}
            if(len(checks) == len(compare)):
                result.append(i - len(p))
        """
        compare = {}
        checks = {}
        counter = 0
        lenP = len(p)
        result = []
        for i in p:
            if(i in compare):
                compare[i] += 1
            else:
                compare[i] = 1

        for i in range(len(s)):
            counter += 1
            if(counter > len(p)):
                if(s[i] in checks):
                    checks[s[i]] += 1
                if(s[i] not in checks and s[i] in compare):
                    checks[s[i]] = 1
                if(s[i - lenP ] in checks):
                    checks[s[i - lenP ]] -= 1
            else:
                if(s[i] in checks):
                    checks[s[i]] += 1
                if(s[i] not in checks and s[i] in compare):
                    checks[s[i]] = 1
            if(checks == compare):
                result.append(i - lenP + 1)
        return result
