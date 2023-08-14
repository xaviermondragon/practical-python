class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """
    def headings(self, headers):
        for header in headers:
            print(f'{header:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for data in rowdata:
            print(f'{data:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format
    """

    def headings(self, headers):
        print('<tr><th>' + '</th><th>'.join(headers) + '</th></tr>')

    def row(self, rowdata):
        print('<tr><td>' + '</td><td>'.join(rowdata) + '</td></tr>')


def create_formatter(format_name):
    """
    Create an appropriate formatter given an output format name
    """
    if format_name == 'txt':
        return TextTableFormatter()
    elif format_name == 'csv':
        return CSVTableFormatter()
    elif format_name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {format_name}')
