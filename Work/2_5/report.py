# report.py
#
# Exercise 2.4

import csv
import rich

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

portfolio = portfolio_reader('../Data/portfolio.csv')

total_cost = 0.0

for item in portfolio:
    total_cost += item['shares'] * item['price']

print(total_cost)