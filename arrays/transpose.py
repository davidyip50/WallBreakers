class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        [[1,2,3],
         [4,5,6],
         [7,8,9]]
         
        [[1,4,7],
         [2,5,8],
         [3,6,9]]
         
         [[1,2,3],
          [4,5,6]]
          
          [[1,4],
           [2,5],
           [3,6]]
        """
        result = []
        num_col = A[0]
        num_row = len(A)
        for col in range(len(num_col)):#2
            new_row = []
            for row in range(num_row):#3
                new_row.append(A[row][col]) #0 0 0 1 0 2
            result.append(new_row)
        return result
