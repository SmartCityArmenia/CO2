#!/usr/bin/env python
from __future__ import print_function

import pymysql
import time

conn = pymysql.connect("212.34.238.190","root","my_password","iot" )
cur = conn.cursor()
cur.execute("SELECT * FROM `sensors`")
print(cur.description)

print()

file = open('data/CO_'+time.strftime("%d-%m-%Y")+'.txt',mode = 'w')

for row in cur:
    #print(str(row[2])[:-2] + "\t" + str(row[3])[:-2] + "\r")
    file.write(str(row[2])[:-2] + "\t" + str(row[3])[:-2] + "\r")
file.close()
cur.close()
conn.close()