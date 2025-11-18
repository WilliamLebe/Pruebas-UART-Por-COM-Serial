import serial

ser = serial.Serial("COM9", 9600, timeout=1)
print("Escuchando en", ser.name)

while True:
    data = ser.readline()
    if data:
        print("PC recibió:", data.decode().strip())
