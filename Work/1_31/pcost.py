def portfolio_cost(filename):
    try:
        with open(filename, 'r') as f:
            headers = next(f)
            total = 0
            for line in f:
                try:
                    symbol, number, price = (x for x in line.split(','))
                    number = int(number)
                    price = float(price)
                    total += number * price
                except ValueError:
                    print(f'Bad row in file: {filename} - {line}')


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
