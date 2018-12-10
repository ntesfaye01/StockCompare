def dynamic_profit_max(prices):
    #
    maximum_profit = 0
    minimum_buy = prices[0]

    for i in range(1, len(prices)):

        if prices[i] < minimum_buy:
            minimum_buy = prices[i]

        if (prices[i] - minimum_buy) > maximum_profit:
            maximum_profit = (prices[i] - minimum_buy)

    return maximum_profit