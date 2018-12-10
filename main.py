import csv

with open('QQQ.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    closePrices = []

    for i in range(20):
        closePrices.append([])

    for row in csv_reader:
        for i in range(20):
            if int(row['Date'][:4]) == i + 1999:
                closePrices[i].append(float(row['Close']))

    for priceYear in closePrices:
        print("=================")
        print("=================")
        print("=================")
        print(priceYear)
        print(len(priceYear))
        print("=================")
        print("=================")
        print("=================")
