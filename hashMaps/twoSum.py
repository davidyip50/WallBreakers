class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        position = {}
        
        for i in range(len(nums)):
            position[nums[i]] = i
            
        for i in range(len(nums)):
            lookup = target - nums[i]
            if(lookup in position and i != position[lookup]):
                return [i,position[lookup]]
