# pcost.py

import csv
import sys
import report


def portfolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    return sum([record['shares'] * record['price'] for record in report.read_portfolio(filename)])


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
