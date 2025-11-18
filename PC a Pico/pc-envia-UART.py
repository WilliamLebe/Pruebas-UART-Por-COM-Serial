import serial

# Abre el puerto del adaptador USB–TTL
ser = serial.Serial("COM9", 9600, timeout=1)
print("Puerto abierto:", ser.name)

while True:
    texto = input("Escribe mensaje para el Pico: ")
    if not texto:
        break
    ser.write((texto + "\n").encode("utf-8"))
    print("Enviado:", texto)
