# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    """ Parse a CSV file into a list of records with type conversion """
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        indices = [headers.index(column_name) for column_name in select]
        headers = select
    else:
        indices = []

    records = []
    for row_number, row in enumerate(rows, 1):
        if not row:  # Skip rows with no data
            continue

        # Filter the row if specific columns were selected
        if indices:
            row = [row[index] for index in indices]

        # Perform type conversion if specific types were given
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {row_number}: Couldn't convert {row}")
                    print(f"Row {row_number}: Reason {e}")
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
