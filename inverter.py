import mysql.connector
from datetime import datetime
from time import sleep
import spidev
import RPi.GPIO as GPIO

#set board numbering mode to BCM because it's what we're using
GPIO.setmode(GPIO.BCM)

#connect to database, change the ip address in host, accordingly if db is in cloud
mydb = mysql.connector.connect(host = 'localhost', user = "ashwath", passwd = 'Avaritia@123', database = 'Inverter', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

#open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

#define custom chip select
CS_ADC = 12
GPIO.setup(CS_ADC, GPIO.OUT)

#define function to read SPI data from ADC
def ReadChannel3008(channel):
  #don't really know how this works, but it does
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2] 
  return data

#define function to convert ADC value to voltage
def ConvertToVoltage(value, bitdepth, vref):
  return vref*(value/(2**bitdepth-1))

i = 1
##loop
while i <= 20:
    ##find out the time now
    now = datetime.now()
    formatted = now.strftime('%Y-%m-%d %H:%M:%S')
    
    ##find voltage
    GPIO.output(CS_ADC, GPIO.LOW)
    value = ReadChannel3008(4)
    GPIO.output(CS_ADC, GPIO.HIGH)
    voltage = ConvertToVoltage(value, 12, 3.3) #for MCP3208 at 3.3V
    # print(voltage)

    #find product number
    product = 1

    ##add values to table
    sql = 'insert into Battery (Product, Timestamp, Voltage) values (%s,%s,%s)'
    values = (product, formatted, voltage)
    mycursor.execute(sql, values)

    i+=1
    mydb.commit()
    sleep(2)

GPIO.cleanup() 
print ("Done")
