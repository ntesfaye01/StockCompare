import csv

def pullData(csv_file_path):
    with open(csv_file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        closePrices = []

        for i in range(20):
            closePrices.append([])

        for row in csv_reader:
            for i in range(20):
                if int(row['Date'][:4]) == i + 1999:
                    closePrices[i].append(float(row['Close']))

    return closePrices

DJIclose = pullData('DJI.csv')
SPYclose = pullData('SPY.csv')
QQQclose = pullData('QQQ.csv')

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