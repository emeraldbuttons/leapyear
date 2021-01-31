#Felix Brucker felix.m.brucker@gmail.com
#Program operates with command-line input
#For example "hw1_p4_cs362.py 2000" would return a response for 2000
#If testing in ENGR server add a "python3 " before command

import sys

year = int(sys.argv[1])
t_mes = "is a leap year"
f_mes = "is not a leap year"

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print( year, t_mes )
        else:
            print( year, f_mes )
    else:
        print( year, t_mes )
else:
    print( year, f_mes )
