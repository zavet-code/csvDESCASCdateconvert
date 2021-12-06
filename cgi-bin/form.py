import os
import cgi
import cgitb
cgitb.enable(display=0,logdir="/var/www/cgi-bin/error-logs")

file_name = "/var/www/cgi-bin/practice/process_practice.py"
f = os.path.abspath(os.path.join(file_name))
try:
    open(f)
except:
    print"This file could not be found!"
form = cgi.FieldStorage(f)
firstname = form.getvalue('firstname')
print firstname
