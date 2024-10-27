def portfolio_cost(filename):
    with open(filename, 'r') as f:
        headers = next(f)
        total = 0
        for line in f:
            symbol, number, price = (x for x in line.split(','))
            number = int(number)
            price = float(price)
            total += number * price

    return total

cost = portfolio_cost('../Data/portfolio.csv')
print('Total cost:', cost)