def bruteForce(marketClosePrices):

    maxProfit = 0

    for buyDay in range(0, len(marketClosePrices)):
        for sellDay in range(buyDay + 1, len(marketClosePrices)):
            currProfit = marketClosePrices[sellDay] - marketClosePrices[buyDay]
            if currProfit > maxProfit:
                maxProfit = currProfit
