import main

def DivideAndConquerSingleSellProfit(arr):

    if len(arr) <= 1:
        return 0;


    left  = arr[ : len(arr) / 2]
    right = arr[len(arr) / 2 : ]

    leftbest  = DivideAndConquerSingleSellProfit(left)
    rightbest = DivideAndConquerSingleSellProfit(right)

    crossbest = max(right) - min(left)

    return max(leftbest, rightbest, crossbest)

# arr = [1,2,3,4,5,6,7,8,9,15]
#print(DivideAndConquerSingleSellProfit(arr))
DJIClose = main.DJI_close_prices
QQQClose = main.QQQ_close_prices
SPYClose = main.SPY_close_prices
for dp in DJIClose:
    DivideAndConquerSingleSellProfit(dp)
for qp in QQQClose:
    DivideAndConquerSingleSellProfit(qp)
for sp in SPYClose:
    DivideAndConquerSingleSellProfit(sp)




