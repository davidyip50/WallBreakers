class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        return the max number in the array?
        compare = first index
        down = len A
        using binary search
        if(mid < compare) still climbing move the first index up
            compare = mid + 1
        if(mid > compare) started descending move the end down
            down = mid - 1
        if(compare >= down):
            return mid
        """
        if(len(A) == 0):
            return 0
        start = 0 #0
        end = len(A) #3
        mid = (start + end) / 2 #0
        while(start <= mid):
            mid = (start + end) / 2
            #print(start,mid,end)
            if(A[mid - 1] < A[mid] and A[mid + 1] < A[mid]):
                print(A[mid-1], A[mid], A[mid+1])
                return mid
            if(A[mid] < A[mid + 1]): 
                start = mid 
            if(A[mid] > A[mid + 1]): 
                end = mid
        #print(start,mid,end)
        return mid
            
