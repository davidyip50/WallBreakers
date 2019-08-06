class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1 2 3 4] = 1 + 3
        [2 4 1 3] = 2 + 1 =  3
        """
        orderNums = sorted(nums)
        total = 0
        for i in range(0,len(nums),2):
            currentTotal = min(orderNums[i], orderNums[i + 1])
            total += currentTotal
        return total
        
