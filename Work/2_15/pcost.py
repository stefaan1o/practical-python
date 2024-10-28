import csv
import sys

def portfolio_cost(filename):
    try:
        with open(filename, 'r') as f:
            rows = csv.reader(f)
            headers = next(rows)
            total = 0
            for index, row in enumerate(rows, start=1):
                try:
                    symbol = row[0]
                    number = int(row[1])
                    price = float(row[2])
                    total += number * price
                except ValueError:
                    print(f'Bad row in : {filename} - {index} {row}')


    except FileNotFoundError:
        print(f'File not found: {filename}')
        return 0
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '../Data/missing.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')