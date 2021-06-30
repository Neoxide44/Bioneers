import serial
import csv
import time

ser1 = serial.Serial('/dev/ttyACM0')
ser1.flushInput()
ser2 = serial.Serial('/dev/ttyACM1')
ser2.flushInput()
ser3 = serial.Serial('/dev/ttyACM2')
ser3.flushInput()
ser4 = serial.Serial('/dev/ttyACM3')
ser4.flushInput()

def save():
    ser1_bytes = ser1.readline()
    ser2_bytes = ser2.readline()
    ser3_bytes = ser3.readline()
    ser4_bytes = ser4.readline()

    write(ser1_bytes, 1)
    write(ser2_bytes, 2)
    write(ser3_bytes, 3)
    write(ser4_bytes, 4)


def write(ser_bytes, i):
    x = ser_bytes[0:len(ser_bytes) - 2].decode("utf-8")
    L = x.split(",")
    named_tuple = time.localtime()

    with open("/media/neoxide44/My Passport/Data/Terrarium " + str(i) + "/T" + str(i) + "data" + str(time.strftime("%m-%d", named_tuple)) + ".csv", "a") as f:
        fieldnames = ['LIGHT', 'TEMPERATURE', 'HUMIDITY', 'TIME']
        row = csv.DictWriter(f, fieldnames=fieldnames)
        if str(time.strftime("%H:%M", named_tuple)) == "00:00":
            row.writeheader()
        if len(L) == 3:
            row.writerow({'LIGHT': L[0], 'TEMPERATURE': L[1], 'HUMIDITY': L[2], 'TIME': str(time.strftime("%H:%M:%S", named_tuple)) })




while True:
    try:
        named_tuple = time.localtime()
        if(str(time.strftime("%M:%S", named_tuple)) == "00:00"):
            save()
            time.sleep(1)
        elif (str(time.strftime("%M:%S", named_tuple)) == "15:00"):
            save()
            time.sleep(1)
        elif (str(time.strftime("%M:%S", named_tuple)) == "30:00"):
            save()
            time.sleep(1)
        elif (str(time.strftime("%M:%S", named_tuple)) == "45:00"):
            save()
            time.sleep(1)
    except:
        named_tuple = time.localtime()
        if (str(time.strftime("%M:%S", named_tuple)) == "00:00"):
            save()
            time.sleep(1)
        elif (str(time.strftime("%M:%S", named_tuple)) == "15:00"):
            save()
            time.sleep(1)
        elif (str(time.strftime("%M:%S", named_tuple)) == "30:00"):
            save()
            time.sleep(1)
        elif (str(time.strftime("%M:%S", named_tuple)) == "45:00"):
            save()
            time.sleep(1)
