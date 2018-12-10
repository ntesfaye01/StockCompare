def bruteForce(marketClosePrices):

    """Finds the maximum profit by comparing all pairs of buy and sell days with the assumption that
    the buy date happens before the sell date."""
    maxProfit = 0

    for buyDay in range(0, len(marketClosePrices)):
        for sellDay in range(buyDay + 1, len(marketClosePrices)):
            currProfit = marketClosePrices[sellDay] - marketClosePrices[buyDay]
            if currProfit > maxProfit:
                maxProfit = currProfit

    return maxProfit