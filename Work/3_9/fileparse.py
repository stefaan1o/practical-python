# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True,delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select requires column headers")

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for index, row in enumerate(rows):
            try:
                if not row:    # Skip rows with no data
                    continue
                # Filter the row if specific columns were selected
                if indices:
                    row = [ row[index] for index in indices ]
                if types:
                    row = [func(val) for func, val in zip(types, row)]

                if has_headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                print(f"Row {index}: Couldn't convert {row}")
                print(f"Row {index}: Reason {e}")

    return records
