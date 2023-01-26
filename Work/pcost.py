# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            total_cost += int(row[1]) * float(row[2])
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
