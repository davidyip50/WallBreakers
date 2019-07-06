class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stop = len(nums)
        result = []
        checks = {}
        
        for i in nums:
            if(i in checks):
                checks[i] += 1
            else:
                checks[i] = 1
        for key in checks:
            if(checks[key] == 2):
                result.append(key)
        
        for i in range(stop):
            if(i+1 not in checks):
                result.append(i+1)
        return result
