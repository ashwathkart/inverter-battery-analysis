import spidev
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

#define custom chip select
#this is done so we can use dozens of SPI devices on 1 bus
CS_ADC = 12
GPIO.setup(CS_ADC, GPIO.OUT)

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel3008(channel):
  #below code sends 00000001 1xxx0000 00000000 to the chip and records the response
  #xxx encodes 0-7, the channel selected for the transfer.
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2] 
  return data

def ConvertToVoltage(value, bitdepth, vref):
  return vref*(value/(2**bitdepth-1))

# Define delay between readings
delay = 1
 
while True:
  GPIO.output(CS_ADC, GPIO.LOW)
  value = ReadChannel3008(4)
  GPIO.output(CS_ADC, GPIO.HIGH)
  voltage = ConvertToVoltage(value, 12, 3.3) #for MCP3208 at 3.3V
  #print(value)
  print(f"{voltage:.3f}")
  # Wait before repeating loop
  time.sleep(delay)
