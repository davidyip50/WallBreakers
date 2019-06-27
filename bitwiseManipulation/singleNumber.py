class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hit = {}
        for key in nums:
            if(key in hit):
                hit[key] += 1
            else:
                hit[key] = 1
        
        for key,val in hit.items():
            if(val == 1):
                return key
        
