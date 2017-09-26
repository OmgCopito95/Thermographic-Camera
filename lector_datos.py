import serial
import time
ser = serial.Serial('COM4', 9600, timeout=0)
while 1:
    try:
        print ser.readline()
    except ser.SerialTimeoutException:
        print('Data could not be read')
    time.sleep(1)