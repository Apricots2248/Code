import csv

def read_csv(ProductStock):
    data = []
    with open(ProductStock, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def write_csv(ProductStock, data):
    with open(ProductStock, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

def edit_csv(ProductStock, row_index, column_index, new_value):
    data = read_csv(ProductStock)
    if row_index < len(data) and column_index < len(data[row_index]):
        data[row_index][column_index] = new_value
        write_csv(ProductStock.csv, data)
        print("CSV file has been updated successfully.")
    else:
        print("Invalid row or column index.")

# Example usage:
# Suppose you have a CSV file named 'data.csv' with the following contents:
# 1,John,Smith
# 2,Jane,Doe
# 3,Bob,Jones

# Now let's edit this file:
edit_csv('data.csv', 1, 1, 'Janet')

# After running this, the content of 'data.csv' will be:
# 1,John,Smith
# 2,Janet,Doe
# 3,Bob,Jones
