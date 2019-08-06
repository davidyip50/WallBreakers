class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        [1,3]
        4  4  -1  -1 
        [3,1,4,5]
         5  9  9  -1  -1  
        [3,5,4,9,8]
         2  2  -1
        [3,1,2]
           2  4  -1
        [3,1,2,4]
        checks = {}
        stack = []
        
        prev = -1
        for i in nums2:
            stack.append(i)
        
        for i in range(len(stack) - 1, -1, -1):
            if(prev > stack[-1] ):
        """
        stack = []
        result = []
        
        for i in nums2:
            stack.append(i)
        
        
        for i in nums1:
            temp = list(stack)
            prev = -1
            while(len(temp) > 0 and temp[-1] != i):
                #print(i)
                if(temp[-1] > i):
                    prev = temp[-1]
                    temp.pop(-1)
                else:
                    temp.pop(-1)
            if(len(temp) == 0):
                prev = -1
            result.append(prev)
        return result
                
