def brute_force(market_close_prices):
    """Function that uses brute force to find the maximum profit by comparing all pairs of buy and sell days with
        the assumption that the buy date happens before the sell date. Takes in an array of market close prices for
        a year, returning the greatest profit to be made buying on one day and selling on one day."""

    max_profit = 0

    for buy_day in range(0, len(market_close_prices)):
        for sell_day in range(buy_day + 1, len(market_close_prices)):
            # if marketClosePrices[buyDay] > budget:
            #     continue
            curr_profit = market_close_prices[sell_day] - market_close_prices[buy_day]
            if curr_profit > max_profit:
                max_profit = curr_profit

    return max_profit



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