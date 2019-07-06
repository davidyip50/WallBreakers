from collections import defaultdict
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        
        i % 2 == j % 2
        means both i and j either need to be even or odd indices
        swapping will result in the same will give same 
        
        find potential groupings:
            we can have a hash map with the key being the sum of the asci and the value being the index of A 
            if the index is odd we add that to a sum_odd vale
            if the index is even we add taht to sum_even value
            if both these values match the stored key add it to the list
            
                        #elif(key in checks and len(checks[key][0][0]) == len(A[i]) and (checks[key][0][1] != sum_odd or checks[key][0][2] != sum_even)):
             #   key += sum_odd
              #  checks[key].append([A[i],sum_odd,sum_even])
        """
        checks = defaultdict(list)
        print(A)
        for i in range(len(A)):
            key = ""
            sum_odd = 0
            sum_even = 0
            #print(str([A[i]]),A[i] )
            for letters in range(len(A[i])):
                if(letters % 2 == 0):
                    sum_even += ord(A[i][letters])
                if(letters % 2 == 1):
                    sum_odd += ord(A[i][letters])
            key = str((sum_even,sum_odd))
            
            if(key in checks):
                checks[key].append([A[i],sum_odd,sum_even])
            elif(key in checks and len(checks[key][0][0]) == len(A[i]) and (checks[key][0][1] != sum_odd or checks[key][0][2] != sum_even)):
                key = str((sum_even,sum_odd * 2))
                checks[key].append([A[i],sum_odd,sum_even])
            else:
                checks[key].append([A[i],sum_odd,sum_even])
            #print( str(key), checks[key])
        print(len(checks))
        return len(checks)
        
        
