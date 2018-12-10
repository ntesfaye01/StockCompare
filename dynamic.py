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


QQQ_maximum_profits = []
for i in range(len(QQQ_close_prices)):
    annual_max_profit = dynamic.dynamic_profit_max(QQQ_close_prices[i])
    QQQ_maximum_profits.append(annual_max_profit)

DJI_maximum_profits = []
for i in range(len(DJI_close_prices)):
    annual_max_profit = dynamic.dynamic_profit_max(DJI_close_prices[i])
    DJI_maximum_profits.append(annual_max_profit)

SPY_maximum_profits = []
for i in range(len(SPY_close_prices)):
    annual_max_profit = dynamic.dynamic_profit_max(SPY_close_prices[i])
    SPY_maximum_profits.append(annual_max_profit)