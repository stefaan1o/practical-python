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
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

portfolio = portfolio_reader('../Data/portfolio.csv')

total_cost = 0.0

for name, shares, price in portfolio:
    total_cost += shares * price

print(total_cost)