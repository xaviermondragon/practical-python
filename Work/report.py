# report.py

import fileparse
from stock import Stock
import tableformat
from portfolio import Portfolio


def read_portfolio(filename, **options):
    """
    Read a stock portfolio file into a list of dictionaries with keys name, shares, and price.
    """
    with open(filename) as lines:
        portfolio_dictionaries = fileparse.parse_csv(lines,
                                                     select=['name', 'shares', 'price'],
                                                     types=[str, int, float],
                                                     **options
                                                     )
        portfolio = [Stock(**d) for d in portfolio_dictionaries]
        return Portfolio(portfolio)


def read_prices(filename):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list and prices dictionary.
    """
    report = []
    for record in portfolio:
        name = record.name
        shares = record.shares
        price = prices[name]
        change = price - record.price
        report.append((name, shares, price, change))

    return report


def print_report(report, formatter):
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, format_name='txt'):
    """
    Make a stock report given portfolio and price data files.
    """
    #  Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(format_name)
    print_report(report, formatter)


def main(args):
    if len(args) == 3:
        portfolio_report(args[1], args[2])
    elif len(args) == 4:
        portfolio_report(args[1], args[2], args[3])
    else:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])


if __name__ == '__main__':
    import sys
    main(sys.argv)

# python3 report.py Data/portfolio.csv Data/prices.csv txt
