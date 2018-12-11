import main

def DivideAndConquer(arr):

    if len(arr) <= 1:
        return 0;


    left  = arr[:len(arr) / 2]
    right = arr[len(arr) / 2:]

    leftMax  = DivideAndConquer(left)
    rightMax = DivideAndConquer(right)

    crossMax = max(right) - min(left)

    return max(leftMax, rightMax, crossMax)

# arr = [1,2,3,4,5,6,7,8,9,15]
VTIClose = main.VTI_close_prices
QQQClose = main.QQQ_close_prices
SPYClose = main.SPY_close_prices
for vp in VTIClose:
    DivideAndConquer(vp)
for qp in QQQClose:
    DivideAndConquer(qp)
for sp in SPYClose:
    DivideAndConquer(sp)





