def dynamic_profit_max(prices):
    """Function that utilizes dynamic programming to find the maximum profit possible for a given ETF. Takes in
    an array of market close prices for a year, returning the greatest profit to be made buying on one day and
    selling on one day."""

    maximum_profit = 0
    minimum_buy = prices[0]

    for i in range(1, len(prices)):

        if prices[i] < minimum_buy:
            minimum_buy = prices[i]

        if (prices[i] - minimum_buy) > maximum_profit:
            maximum_profit = (prices[i] - minimum_buy)

    return maximum_profit