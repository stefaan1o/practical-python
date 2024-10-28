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

def make_report(prices,portfolio):
    report = []
    for item in portfolio:
        price = item['price']
        price_actual = prices[item['name']]
        change = price_actual - price
        report.append((item['name'], item['shares'], price_actual, change))
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')

    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- -----------')

    for name, shares, price, change in report:
        price_print = f'${price:.2f}'
        print(f'{name:>10s} {shares:>10d} {price_print:>10s} {change:>10.2f}')


prices = read_prices('../Data/prices.csv')
portfolio = portfolio_reader('../Data/portfolio.csv')
report = make_report(prices,portfolio)
print_report(report)