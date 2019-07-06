class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        checks = {}
        result = {}
        result2 = []
        for i in nums1:
            if(i in checks):
                checks[i] += 1
            else:
                checks[i] = 1
        
        for i in nums2:
            if(i in checks and i in result):
                result[i] += 1
            if(i in checks and i not in result):
                result[i] = 1
        
        for keys in result.keys():
            result2.append(keys)
        
        return result2
        
