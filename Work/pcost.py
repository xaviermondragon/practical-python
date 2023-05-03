# pcost.py
#
# Exercise 2.16
import csv
import sys


def portfolio_cost(name_of_file):
    """Computes the total cost (shares*price) of a portfolio file"""
    total_cost = 0.0

    with open(name_of_file, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row_number, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                number_of_shares = int(record['shares'])
                price = float(record['price'])
                total_cost += number_of_shares * price
            except ValueError:
                print(f'Row {row_number}: Couldn\'t convert: {row}')
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
