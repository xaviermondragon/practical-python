# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(name_of_file):
    """Computes the total cost (shares*price) of a portfolio file"""
    total_cost = 0.0

    with open(name_of_file, 'rt') as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            number_of_shares = int(row[1])
            price = float(row[2])
            total_cost += number_of_shares * price
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
