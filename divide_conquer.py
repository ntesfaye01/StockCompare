import main

def divide_and_conquer(market_close_prices):
    """Function that utilizes divide and conquer to find the maximum profit possible for a given ETF. Takes in
        an array of market close prices for a year, returning the greatest profit to be made buying on one day and
        selling on one day."""

    if len(market_close_prices) <= 1:
        return 0;

    left = market_close_prices[:len(market_close_prices) / 2]
    right = market_close_prices[len(market_close_prices) / 2:]

    left_max = divide_and_conquer(left)
    right_max = divide_and_conquer(right)

    cross_max = max(right) - min(left)

    return max(left_max, right_max, cross_max)

# arr = [1,2,3,4,5,6,7,8,9,15]
VTIClose = main.VTI_close_prices
QQQClose = main.QQQ_close_prices
SPYClose = main.SPY_close_prices
for vp in VTIClose:
    divide_and_conquer(vp)
for qp in QQQClose:
    divide_and_conquer(qp)
for sp in SPYClose:
    divide_and_conquer(sp)





