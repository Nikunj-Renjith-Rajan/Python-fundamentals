# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
def maxProfit(prices):
        m=prices[0]
        profit=0
        for i in range(len(prices)):
            if prices[i]<m:
                m=prices[i]
            if prices[i]-m>profit:
                profit=prices[i]-m
        return profit
print(maxProfit([7,1,5,3,6,4]))                 #Max profit=5 because 6-1
print(maxProfit([7,6,5,3,2,1]))                 #No profit because stock price keeps falling