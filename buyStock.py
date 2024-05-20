class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        leftPointer, rightPointer = 0, 1
        maxProfit = 0
        while rightPointer < len(prices):
            if prices[leftPointer] < prices[rightPointer]:
                profit = prices[rightPointer] - prices[leftPointer]
                maxProfit = max(profit, maxProfit)

            else:
                leftPointer = rightPointer
            rightPointer += 1

        return maxProfit 




######## 50% correct #######
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         buyStockPrice = prices[0]
#         buingDay = 0
#         day = 0
#         d = 0
#         for price in prices:
#             if buyStockPrice > price:
#                 buyStockPrice = price
#                 buingDay = day
#             day = day + 1
#         print("buyStockPrice===",buyStockPrice)
#         print("buingDay===",buingDay)
#         sellPrice = buyStockPrice


#         for p in prices:
#             if p > sellPrice and buingDay < d:
#                 sellPrice = p
#                 print("sellPrices inside",sellPrice)
#             d = d + 1
#         print("sellPrices outside",sellPrice)
#         return sellPrice - buyStockPrice

# # Create an object of the Solution class
# solution = Solution()

# # Define the sample data
# # sample_data = [7, 1, 5, 3, 6, 4]
# sample_data = [2,4,1]


# # Call the maxProfit function with the sample data
# result = solution.maxProfit(sample_data)

# # Print the result
# print(result)  # Output: 5




