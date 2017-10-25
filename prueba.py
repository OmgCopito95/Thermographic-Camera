import serial
import time
ser = serial.Serial('COM4', 9600, timeout=0)

def comenzar():
    while True:
        try:
            print ser.write("1")
            time.sleep(9)
        except ser.SerialTimeoutException:
            print('Data could not send')

def detener(): 
    try:
        ser.write("2")
        time.sleep(9)
    except ser.SerialTimeoutException:
            print('Data could not send')    

