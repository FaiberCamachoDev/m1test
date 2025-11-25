import csv

def read_csv(path):
    data = []
    """
    read a CSV file and return a list of row (without header).
    """
    try:
        with open(path, "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader) 
            for row in reader:
                item = {header[i]: row[i] for i in range(len(header))}
                data.append(item)
    except FileNotFoundError:
        print("File not founded.")
    return data

def write_csv(path, data):
    """
    overwrite a csv file with header + data.
    'data' would be a list where data[0] is the header.
    """
    if not data:
        raise ValueError("Cannot write a empty CSV file.")

    header = data[0]
    rows = data[1:]

    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

def append_csv(path, row):
    """
    add a new row in csv file
    """
    with open(path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

def save_csv(path, data):
    """
    function for save a csv file
    """
    if not data:
        print("No data to save.")
        return
    header = list(data[0].keys())
    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for item in data:
            writer.writerow([item[key] for key in header])