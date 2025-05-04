import serial
import time

# UART portunu aç
ser = serial.Serial("/dev/serial0", 9600, timeout=1)

# Alıcı adres ve kanal bilgileri
address_high = b'\x00' # Target address high, ADDH, 0 
address_low = b'\x36' # Target address low, ADDl, 54 
channel = b'\x0c'  # Target channel, CHAN , 12

ser.reset_input_buffer()  # Giriş buffer'ını temizle
ser.reset_output_buffer()  # Çıkış buffer'ını temizle

ser.write(address_high)
ser.write(address_low)
ser.write(channel)
ser.write(b'Merhaba')

    

