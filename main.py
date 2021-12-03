import eel
import csv
import io
import re
from datetime import datetime

eel.init('web')

eel.start('main.html', size=(700, 700))

main_csv = 'eggs1.csv'
sorted_csv = 'example.csv'


def date_key(row):
    return datetime.strptime(row[9].strip(), "%d/%b/%y %H:%M %p")

def ticket_number_key(row):
    result = re.findall('\d+', row[1])
    return result

def letter_key(row):
    result = re.findall('\w+', row[3])
    return result

def csv_writer(text, file_path, nline):
    s = io.StringIO(text)
    with open(file_path, 'a', newline='') as f:
        for line in s:
            f.write(line + nline)

@eel.expose
def get_sort_csv(main_csv, delim , rev):           #delim = '|' rev = True or False
    with open(main_csv, newline='') as csvfile:
        first_line = csvfile.readline()
        spamreader = list(csv.reader(csvfile, delimiter = delim))
        spamreader.sort(key = letter_key, reverse = False)
        csv_writer(first_line, sorted_csv, '')
        for row in spamreader:
            csv_writer('| '.join(row), sorted_csv, '\n')
            print(datetime.strptime(row[9].strip(), "%d/%b/%y %H:%M %p"))
            print('| '.join(row))
