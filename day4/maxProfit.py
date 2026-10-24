class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                current_profit = prices[i] - buy
                if current_profit > profit:
                    profit = current_profit

        return profit

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
