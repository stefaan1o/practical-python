import csv

def portfolio_cost(filename):
    try:
        with open(filename, 'r') as f:
            rows = csv.reader(f)
            headers = next(rows)
            total = 0
            for row in rows:
                try:
                    symbol = row[0]
                    number = int(row[1])
                    price = float(row[2])
                    total += number * price
                except ValueError:
                    print(f'Bad row in file: {filename} - {row}')


    except FileNotFoundError:
        print(f'File not found: {filename}')
        return 0
    return total

cost = portfolio_cost('../Data/missing2.csv')
print('Total cost:', cost)

cost = portfolio_cost('../Data/portfolio.csv')
print('Total cost:', cost)

cost = portfolio_cost('../Data/missing.csv')
print('Total cost:', cost)
