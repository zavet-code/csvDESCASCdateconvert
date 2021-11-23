import csv
import re
from datetime import datetime

def date_key(row):
    return datetime.strptime(row[9].strip(), "%d/%b/%y %H:%M %p")

with open('eggs.csv', newline='') as csvfile:
    spamreader = list(csv.reader(csvfile, delimiter=','))
    spamreader.sort(key=date_key)
    for row in spamreader:
        print(datetime.strptime(row[9].strip(), "%d/%b/%y %H:%M %p"))
        print(', '.join(row))
        






        #for item in row:
            #match = re.search('\d\d/\w{3}/\d\d \d:\d\d \w\w', item)
            #if match:
                #li = item.split()
                #li[1] = '0' + li[1]
                #item =' '.join(li)
                #print(', '.join(row))
            #else: 
                #pass
        




