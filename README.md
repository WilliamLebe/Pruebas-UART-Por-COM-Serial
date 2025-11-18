# Comunicación UART entre PC y Raspberry Pi Pico
Este repositorio contiene dos ejemplos funcionales para probar comunicación UART entre un PC y una Raspberry Pi Pico usando:

- Adaptador USB–TTL (PC <-> Pico)
- MicroPython en la Pico
- Python (pySerial) en el PC

## 📁 Estructura del proyecto

```
/PC_A_PICO
    pc-envia-UART.py      # Script para enviar datos desde el PC al Pico

/PICO_A_PC
    UART_2.py             # Script MicroPython para enviar datos desde el Pico al PC
```

---

# 📝 1. Comunicación **PC → Pico**

### 📌 Archivos:
- **pc-envia-UART.py** (carpeta *PC_A_PICO*)
- **UART_RX.py** (corriendo en la Pico)

### ▶ ¿Qué hace?
El PC envía mensajes por el puerto COM (adaptador USB–TTL) y la Pico los recibe y los muestra por consola.

### 🔌 Conexiones (PC → Pico)
| Adaptador USB–TTL | Pico |
|------------------|------|
| **TXD** | GP1 (RX) |
| **RXD** | GP0 (TX) |
| **GND** | GND |
| **5V ó 3.3V** | VSYS |

### ▶ Ejecutar en PC
```python pc-envia-UART.py```

Te pedirá que escribas mensajes y los enviará al Pico.

---

# 📝 2. Comunicación **Pico → PC**

### 📌 Archivos:
- **UART_2.py** (carpeta *PICO_A_PC*)
- Un script en PC para leer datos (ej: pc-lee-UART.py)

### ▶ ¿Qué hace?
La Pico envía un texto cada segundo por UART y el PC lo recibe y lo imprime en pantalla.

### 🔌 Conexiones (Pico → PC)
| Pico | Adaptador USB–TTL |
|------|-------------------|
| GP0 (TX) | RXD |
| GP1 (RX) | TXD |
| GND | GND |
| VSYS | 5V ó 3.3V |

---

# 🚀 ¿Cómo usar este repositorio?

1. Conecta tu adaptador USB–TTL al PC.
2. Verifica en el Administrador de Dispositivos el número de COM.
3. Conecta TX ↔ RX, GND ↔ GND, VCC ↔ VSYS.
4. Carga el archivo correspondiente en la Pico (Thonny).
5. Ejecuta el script de PC para enviar o recibir datos.

---

# 📌 Requisitos

### Para PC:
- Python 3
- Biblioteca `pyserial`
```pip install pyserial```

### Para Raspberry Pi Pico:
- Thonny IDE
- MicroPython instalado en la Pico

---

# Proyecto desarrollado para pruebas de comunicación UART en laboratorio de **Telecomunicaciones UMNG 2025**.

Autor: William Leon con códigos base de Jose Rugeles 
