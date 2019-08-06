class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid = int(len(nums) / 2) #3 5
        start = 0 #
        end = len(nums) #
        while(end >= start and mid < len(nums)):
            if(target == nums[mid]):
                return mid
            if(target < nums[mid]): #120 < 5
                end = mid - 1  #
                mid = int((end + start) / 2) #
            if(target > nums[mid]): # 120 > 12
                start = mid + 1 # 6
                mid = int((start + end)/2) # 6 + 6 /  2 = 6
        return -1
        
