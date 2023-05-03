# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    """Opens a given portfolio file and reads it into a dictionary"""
    portfolio = []

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            holding = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
            }
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    file = open(filename, 'r')
    rows = csv.reader(file)
    prices = {}

    for row in rows:
        try:
            prices[row[0]] = float(row[1])
        except IndexError:
            pass

    return prices


def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        price = prices[name]
        change = price - stock['price']
        report.append((name, shares, price, change))

    return report


#portfolio = read_portfolio('Data/portfolio.csv')
portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

# Print report
headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {"${:.2f}".format(price):>10s} {change:>10.2f}')
