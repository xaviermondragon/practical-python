# report.py

import fileparse
import stock


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys name, shares, and price.
    """
    with open(filename) as lines:
        stock_dictionaries = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
        return [stock.Stock(d['name'], d['shares'], d['price']) for d in stock_dictionaries]


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


def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)

# python3 report.py Data/portfolio.csv Data/prices.csv
