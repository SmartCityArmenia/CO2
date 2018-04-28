#!/usr/bin/python3

import pymysql
import time
import serial.tools.list_ports
import serial,sys,os

print("----HI!----")

id = 1
list = serial.tools.list_ports.comports()
print("COM port device: ")

for el in list:
    print('device: ',el.device, el.description)
print(sys.argv)
#dev = input('input device id: /dev/ttyUSB')
dev = '/dev/ttyUSB'+str(sys.argv[1])
#str(dev)
try:
    ser = serial.Serial(dev)
    ser.write(b'\r')
    time.sleep(3)
except:
    print("Sensor don't connected!")
    sys.exit(0)
print('---Sensor Initial OK---')

while True:
    i=0
    score = 0
    count = 0
    while i<15:
        try:
            ser.write(b'\r')
            read = str(ser.readline())[2:-5]
            l = read.split(', ')
            score = score + int(l[id])
            count = count+1
            print(l[id])
            time.sleep(59)
            i = i+1
        except KeyboardInterrupt:
            print("Stoped from keyboard")
            #os.execl(sys.executable, sys.executable, *sys.argv)
            sys.exit()

    sql = "INSERT INTO `sensors`(sens_id, date_time, CO2) VALUES (NULL,"+str(int(time.time()))+","+str(int(score/count))+")"
    try:
        db = pymysql.connect("212.34.238.190","root","my_password","iot" )
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
    except:
        print('---ERROR: Server error, initial or upload---')
        try:
            db = pymysql.connect("212.34.238.190","root","my_password","iot" )
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
        except:
             print("AAAAAAAAAAAAAAAAAAAA!!!!! apocalips, I'm going, goodbye")
             os.execl(sys.executable, sys.executable, *sys.argv)
             sys.exit(0)
