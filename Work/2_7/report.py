# report.py
#
# Exercise 2.4

import csv

def portfolio_reader(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = dict(
                name=row[0],
                shares=int(row[1]),
                price=float(row[2])
            )
            portfolio.append(holding)
    return portfolio


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

portfolio = portfolio_reader('../Data/portfolio.csv')

cost = 0
for s in portfolio:
    cost += s['shares'] * s['price']

value = 0

for item in portfolio:
    price = item['price']
    price_actual = prices[item['name']]
    delta = price - price_actual
    value = value + item['shares'] * price_actual
    print(f"{item['name']} {item['shares']}  {item['price']} {prices[item['name']]}  {delta:.2f}")

print(f"Total cost: {cost:.2f}")
print(f"Total value: {value:.2f}")