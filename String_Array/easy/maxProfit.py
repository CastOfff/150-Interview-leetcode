class Solution(object):
    def maxProfit(self, prices):
        Profit = 0
        minPrice = prices[0]
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if prices[i] > minPrice:
                Profit = max(Profit,prices[i] - minPrice)
        return Profit
        """
        :type prices: List[int]
        :rtype: int
        """
test_1 = Solution()
prices = [7,1,5,3,6,4]
print(test_1.maxProfit(prices))