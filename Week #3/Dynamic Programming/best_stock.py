class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        if(len(prices) == 0):
            return 0
        if(len(prices) == 1):
            return 0
        if(len(prices) == 2 and prices[1] >= prices[0]):
            return prices[1] - prices[0]
        else:
            
            if(len(prices) > 1 and prices[0] > prices[1]):
                prices.remove(prices[0])
            y = 0
            if(len(prices) > 1 and prices[1] >= prices[0]):
                y = prices[1] - prices[0]
                #print(y)
            if(len(prices) > 1 and prices[0] <= prices[1]):
                prices.remove(prices[1])
                
            x = max(y,self.maxProfit(prices))
            
            return x
        """
        if(len(prices) == 0):
            return 0
        low = prices[0]
        for i in range(len(prices)):
            if(prices[i] < low):
                low = prices[i]
            prices[i] = prices[i] - low
        return max(prices)
                
