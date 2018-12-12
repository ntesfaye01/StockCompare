import csv
import time
import dynamic_programming as dynamic

def pullData(csv_file_path):
    with open(csv_file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        closePrices = []

        for i in range(18):
            closePrices.append([])

        for row in csv_reader:
            for i in range(20):
                if int(row['Date'][:4]) == i + 2001:
                    closePrices[i].append(float(row['Close']))

    return closePrices

VTI_close_prices = pullData('VTI.csv')
SPY_close_prices = pullData('SPY.csv')
QQQ_close_prices = pullData('QQQ.csv')


#Dynamic Programming Results
QQQ_maximum_profits = []
for i in range(len(QQQ_close_prices)):
    annual_max_profit = dynamic.dynamic_profit_max(QQQ_close_prices[i])
    QQQ_maximum_profits.append(annual_max_profit)

DJI_maximum_profits = []
for i in range(len(VTI_close_prices)):
    annual_max_profit = dynamic.dynamic_profit_max(VTI_close_prices[i])
    DJI_maximum_profits.append(annual_max_profit)

SPY_maximum_profits = []
for i in range(len(SPY_close_prices)):
    annual_max_profit = dynamic.dynamic_profit_max(SPY_close_prices[i])
    SPY_maximum_profits.append(annual_max_profit)

startTime = time.time()

for cp in QQQ_close_prices*400:
    dynamic.dynamic_profit_max(cp)

endTime = time.time()
print("Final time: " + str(endTime - startTime))