# report.py

import fileparse


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys name, shares, and price.
    """
    return fileparse.parse_csv(filename, types=[str, int, float])


def read_prices(filename):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    return dict(fileparse.parse_csv(filename, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list and prices dictionary.
    """
    report = []
    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        price = prices[name]
        change = price - stock['price']
        report.append((name, shares, price, change))

    return report


def print_report(report):
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {"${:.2f}".format(price):>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    """
    Make a stock report given portfolio and price data files.
    """
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')