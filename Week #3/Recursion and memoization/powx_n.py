class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if(n == 0):
            return 1
        
        
        if(n > 0):
            if(n % 2 == 1):
                a = self.myPow(x,n / 2)
                x = x * a * a
                #ax * self.myPow(x,n / 2) * self.myPow(x,n/2)
                #return x
            else:
                a = self.myPow(x,n / 2)
                x = a * a
                #return x
        if(n < 0):
            if(abs(n) % 2 == 1):
                a = self.myPow(x,-(abs(n)/2))
                x = (1 / x) * a * a
                #return x
            else:
                a = self.myPow(x,-(abs(n)/2))
                x = a * a
                #return x
        return x
            
        
