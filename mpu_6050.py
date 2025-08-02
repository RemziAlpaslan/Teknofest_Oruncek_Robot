from mpu6050 import mpu6050
"""
pip install mpu6050-raspberrypi --break-system-packages
"""

def read_mpu6050():
    try:
        sensor = mpu6050(0x69)
        accel_data = sensor.get_accel_data()
        gyro_data = sensor.get_gyro_data()
        return (accel_data, gyro_data)
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None

if __name__ == "__main__":
    result = read_mpu6050()
    if result:
        accel_data, gyro_data = result
        print("Accelerometer:", accel_data)
        print("Gyroscope:", gyro_data)
    else:
        print("MPU6050 verisi alınamadı.")
