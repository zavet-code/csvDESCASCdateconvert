import csv
import io
import re
from datetime import datetime

main_csv = 'eggs1.csv'
sorted_csv = 'example.csv'


def date_key(row):
    return datetime.strptime(row[9].strip(), "%d/%b/%y %H:%M %p")

def ticket_number_key(row):
    result = re.findall('\d+', row[1])
    return result

def csv_writer(text, file_path, nline):
    s = io.StringIO(text)
    with open(file_path, 'a', newline='') as f:
        for line in s:
            f.write(line + nline)
            

with open(main_csv, newline='') as csvfile:
    first_line = csvfile.readline()
    spamreader = list(csv.reader(csvfile, delimiter='|'))
    spamreader.sort(key=ticket_number_key)
    csv_writer(first_line, sorted_csv, '')
    for row in spamreader:
        csv_writer('| '.join(row), sorted_csv, '\n')
        print(datetime.strptime(row[9].strip(), "%d/%b/%y %H:%M %p"))
        print('| '.join(row))

 
        





