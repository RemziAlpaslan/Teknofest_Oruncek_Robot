import time
from mpu6050 import mpu6050
# mpu6050 kütüphaneyi indirmek için terminale: pip install mpu6050-raspberrypi --break-system-packages yazmalısınız.

def mpu6050_read(sensor_type):
    try:
        
        # MPU6050 nesnesini oluştur
        mpu = mpu6050(0x68)
        
        if sensor_type == "accel":
            data = mpu.get_accel_data()
            return data['x'],data['y'],data['z']

        elif sensor_type == "gyro":
            data = mpu.get_gyro_data()
            return data['x'],data['y'],data['z']
            
        elif sensor_type == "temp":
            data = mpu.get_temp()
            return data

        else:
            return "Hata: Geçersiz sensör tipi! 'accel', 'gyro' veya 'temp' girin."

    except Exception as e:
        return f"Hata oluştu: {e}"

# Örnek kullanım
print(mpu6050_read("accel"))
print(mpu6050_read("gyro"))
print(mpu6050_read("temp"))
