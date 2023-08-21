# pcost.py

import sys
import report


def portfolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    cost = portfolio_cost(filename)
    print(f'Total cost: {cost}')


if __name__ == '__main__':
    import sys
    main(sys.argv)

# python3 pcost.py Data/portfolio.csv
