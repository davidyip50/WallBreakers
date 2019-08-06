import heapq
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        checks = defaultdict(int)
        heapq.heapify(nums)
        for i in nums:
            checks[i] += 1
        result = heapq.nlargest(k,checks.keys(),key = lambda x: checks[x])
        return result
        #print checks
        
        
