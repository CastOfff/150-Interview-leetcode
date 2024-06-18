class Solution(object):
    def maxProfit(self, prices):
        Profit = 0
        idxMin = 0
        for i in range(len(prices)):
            if prices[i] > prices[idxMin]:
                Profit += (prices[i] - prices[idxMin])
                idxMin = i 
            else:
                if prices[i] <  prices[idxMin]:
                    idxMin = i 
        return Profit
        """
        :type prices: List[int]
        :rtype: int
        """
