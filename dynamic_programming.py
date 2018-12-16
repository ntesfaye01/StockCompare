def dynamic_profit_max(market_close_prices):
    """Function that utilizes dynamic programming to find the maximum profit possible for a given ETF. Takes in
        an array of market close prices for a year, returning the greatest profit to be made buying on one day and
        selling on one day."""

    maximum_profit = 0
    minimum_buy = market_close_prices[0]

    for i in range(1, len(market_close_prices)):

        if market_close_prices[i] < minimum_buy:
            minimum_buy = market_close_prices[i]

        if (market_close_prices[i] - minimum_buy) > maximum_profit:
            maximum_profit = (market_close_prices[i] - minimum_buy)

    return maximum_profit