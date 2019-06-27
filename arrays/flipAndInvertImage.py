class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        [[1,1,0],
         [1,0,1],
         [0,0,0]]
         
        [[0,1,1],
         [1,0,1],
         [0,0,0]] 
         
        [[1,0,0],
         [0,1,0],
         [1,1,1]]
        """
        result = []
        numCols = len(A)
        for row in range(len(A)):
            new_row = []
            for col in range(numCols - 1,-1,-1):
                if(A[row][col] == 1):
                    new_row.append(0)
                else:
                    new_row.append(1)
            result.append(new_row)
        return result
                
