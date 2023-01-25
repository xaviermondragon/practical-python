# pcost.py
#
# Exercise 1.27
total_cost = 0.0

with open('Data/portfolio.csv', 'rt') as file:
    next(file)

    for line in file:
        stock = line.split(',')
        total_cost += int(stock[1]) * float(stock[2])

print(f'Total cost: {total_cost}')
