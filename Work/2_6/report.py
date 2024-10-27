# report.py
#
# Exercise 2.4

import csv
import rich

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                symbol = row[0]
                price = float(row[1])
                prices[symbol] = price
            except IndexError as e:
                print(f'row {row} - error: {e}')
                continue
    return prices

prices = read_prices('../Data/prices.csv')
