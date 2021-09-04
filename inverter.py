import mysql.connector
from datetime import datetime
from time import sleep
from random import randint

mydb = mysql.connector.connect(host = 'localhost', user = "ashwath", passwd = 'Avaritia@123', database = 'Inverter', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

i = 1
##loop
while i<=20:
    ##find out the time now
    now = datetime.now()
    formatted = now.strftime('%Y-%m-%d %H:%M:%S')
    
    ##find voltage and current
    voltage = randint(10,12)
    current = randint(90,120)

    

    ##add values to table
    sql = 'insert into Battery (Product, Timestamp, Voltage, Current) values (%s,%s,%s,%s)'
    values = ('1',formatted, voltage, current)
    mycursor.execute(sql, values)

    i+=1
    mydb.commit()
    sleep(2)

print ("Done")