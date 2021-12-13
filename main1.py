import csv
import io
import re
from datetime import datetime


filename = datetime.utcnow().strftime('%Y-%m-%d %H_%M_%S.%f')[:-3]
sorted_csv = 'sortedcsv ' + "%s.csv"% filename

def date_key(row):
    return datetime.strptime(row[9].strip(), "%d/%b/%y %H:%M %p")       #Номер столбца можно поменять если не совпадает, например row[9] на row[8]. Нумерация столбцов начинается с нуля

def number_key(row):
    result = re.findall('\d+', row[2])                                  #Номер столбца можно поменять для каждого ключа!
    return result

def letter_key(row):
    result = re.findall('\w+', row[3])
    return result

def csv_writer(text, file_path, nline):
    s = io.StringIO(text)
    with open(file_path, 'a', newline='') as f:
        for line in s:
            f.write(line + nline)


def get_sort_csv(main_csv, delim , rev):           #delim = '|' rev = True or False
    with open(main_csv, newline='') as csvfile:
        first_line = csvfile.readline()
        spamreader = list(csv.reader(csvfile, delimiter = delim))
        spamreader.sort(key = number_key, reverse = rev)     #number_key = сортировка по числам(игнорируются другие символы) letter_key = сортировка по буквам(игнорируются другие символы)
        csv_writer(first_line, sorted_csv, '')               #date_key = сортировка по дате вида (17/Jul/20 3:38 PM)
        for row in spamreader:
            csv_writer(delim.join(row), sorted_csv, '\n')
            print(delim.join(row))


get_sort_csv('eggs.csv', '|' , True)           # 1 Имя файла пример 'testCSV.csv', 2 delimiter примеры:'|' ',' ';' , 3 True = сортировка по убыванию; False = сортировка по возрастанию
