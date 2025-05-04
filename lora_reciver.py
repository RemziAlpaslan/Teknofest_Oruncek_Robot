import serial
import time

ser = serial.Serial("/dev/serial0", 9600, timeout=1)


ser.reset_input_buffer()  # Giriş buffer'ını temizle
ser.reset_output_buffer()  # Çıkış buffer'ını temizle

while True:
   response = "" 
   while ser.in_waiting:
        response += ser.readline().decode('utf-8', errors="ignore").strip()+" "     
        print(response)
   time.sleep(0.1)
    