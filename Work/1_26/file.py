with open('../Data/portfolio.csv', 'r') as f:
    for line in f:
        row = line.split(',')
        print(row)