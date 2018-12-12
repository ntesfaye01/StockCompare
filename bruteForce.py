import time
import main
def bruteForce(marketClosePrices):


    """Finds the maximum profit by comparing all pairs of buy and sell days with the assumption that
    the buy date happens before the sell date."""
    maxProfit = 0

    for buyDay in range(0, len(marketClosePrices)):
        for sellDay in range(buyDay + 1, len(marketClosePrices)):
            # if marketClosePrices[buyDay] > budget:
            #     continue
            currProfit = marketClosePrices[sellDay] - marketClosePrices[buyDay]
            if currProfit > maxProfit:
                maxProfit = currProfit

    return maxProfit



#Increasing the time we are allowed to buy and sell
"""Multiplying the array of arrays adds n more arrays or subproblems,
so we repeat one case n times. """

# multiplier = 2
# prices = main.QQQ_close_prices.copy() #Changing the amount of buy/sell days in subarrays
# for i in range(0, len(prices)):
#     prices[i] = prices[i] * multiplier
# print(len(prices[0]))  # Should be double the amount expected
#
# startTime = time.time()
# for yearlyCloses in main.QQQ_close_prices: # replacing main.QQQ_close_prices with prices
#     bruteForce(yearlyCloses)                # shows that the time incraese is definetely not linear
# endTime = time.time()
# print("")
# print("Final time: " + str(endTime - startTime))


# print("")
# for yearlyCloses in main.SPY_close_prices:
#     print(bruteForce(yearlyCloses, 999999999))

# print("")
# for yearlyCloses in main.VTI_close_prices:
#     print(bruteForce(yearlyCloses, 999999999))