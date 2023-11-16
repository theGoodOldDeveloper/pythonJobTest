import csv
from pathlib import Path
def write_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in data:
           csv_writer.writerow(row)