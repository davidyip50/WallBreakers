class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1,2,3,1,3,10] = 13
        1 + 3 = 4
        1 + 1 = 2
        1 + 3 + 3 = 7
        2 + 1 = 3
        2 + 1 + 10 = 13
        2 + 2 = 4
        3 + 3 + 1 = 6
        
        [1,2,10,4,5,10]
        
        1 10 4 5 sum(10 5)
        2 4 5 10 sum(4 10)
        10 5 10 1 sum(5 1)
        4 10 1 2 sum(10 2)
        5 1 2 10 sum(1 10)
        10 2 10 4 sum(4 2)
        
        1 10 4 5 sum(10 5)
        2 4 5 10 sum(4 10)
        10 5 10 1
        4 10
        
        10 2
        
        some of the house are already calculated
        
        find highest sum of things that are not next to each other
        
        
        my alg is only checking the next neighbor, but it needs to check the 2 neighbors down or more
        [6,3,10,8,2,10,3,5,10,5,3]
        """
        if(len(nums) == 0):
            return 0
        start = 0
        neighbor = 1
        temp = list(nums)
        results = []
        while(neighbor != len(nums)):
            for i in range(neighbor + 1,len(nums)):
                #find nei
                if(i != start + 1 and i != (start + len(nums) - 1) % len(nums)):
                    temp[i] = nums[start] + nums[i]
                    results.append(nums[start] + nums[i])
                    #find the last robbed house might have some issuses
                    if(i - 2 > neighbor):
                        high = temp[i-2] + nums[i]
                        for test in range(i - 2, neighbor,-1):
                            if(nums[test] + nums[i] > high):
                                high = nums[test] + nums[i]
                                temp[test] = high
                        results.append(high)
                        temp[i] = high
            start += 1
            neighbor += 1
            temp = list(nums)
        #print(results)
        if(len(results) == 0):
            return max(nums)
        return max(results)
            
            
        
        
