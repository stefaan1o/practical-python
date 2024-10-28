# pcost.py
#
# Exercise 1.27
with open('../Data/portfolio.csv', 'r') as f:
    headers = next(f)
    total = 0
    for line in f:
        symbol, number, price = (x for x in line.split(','))
        number = int(number)
        price = float(price)
        total += number * price
print(f'Total cost: {total}')