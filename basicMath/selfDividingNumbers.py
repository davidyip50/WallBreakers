class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left,right + 1, 1):
            check = 0;
            temp = i;
            isDividing = True;
            while(temp != 0):
                check = temp % 10
                temp = temp / 10
                if(check == 0):
                    isDividing = False
                    break
                if( i % check != 0):
                    isDividing = False
                    break
            if(isDividing):
                result.append(i)
        return resultads
