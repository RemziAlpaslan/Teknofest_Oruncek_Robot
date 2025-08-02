import time
import board
# board kütüphaneyi indirmek için terminale: pip install board --break-system-packages yazmalısınız.
import busio
# busio kütüphaneyi indirmek için terminale:  pip install board --break-system-packages yazmalısınız.
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
# adafruit_ads1x15.ads1115 kütüphaneyi indirmek için terminale: pip install adafruit-circuitpython-ads1x15 --break-system-packages yazmalısınız.

import Adafruit_BMP.BMP085 as BMP085
"""
sudo apt-get install python3-smbus i2c-tools
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python3 setup.py install
cd ..

git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
sudo python3 setup.py install
"""
import smbus2
import time

import serial
import pynmea2

"""
pip install pyserial pynmea2 --break-system-packages
"""
from mpu6050 import mpu6050
"""
pip install mpu6050-raspberrypi --break-system-packages
"""

def read_ads1115(channel):
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
        channels = {"A0": ADS.P0, "A1": ADS.P1, "A2": ADS.P2, "A3": ADS.P3}
        if channel not in channels:
            return f"Hata: Geçersiz kanal seçimi ({channel})"
        chan = AnalogIn(ads, channels[channel])
        time.sleep(0.05)
        return chan.voltage
    except Exception as e:
        return f"ADS1115 Hatası: {e}"


def read_bmp180():
    try:
        sensor = BMP085.BMP085(busnum=1)
        return {
            "temperature": sensor.read_temperature(),
            "pressure": sensor.read_pressure(),
            "altitude": sensor.read_altitude()
        }
    except Exception as e:
        return f"BMP180 Hatası: {e}"


def read_rtc_time():
    try:
        DS1307_ADDRESS = 0x68
        bus = smbus2.SMBus(1)

        def bcd_to_dec(val): return (val // 16 * 10) + (val % 16)

        data = bus.read_i2c_block_data(DS1307_ADDRESS, 0x00, 7)
        return {
            "hour": bcd_to_dec(data[2]),
            "minute": bcd_to_dec(data[1]),
            "second": bcd_to_dec(data[0] & 0x7F),
            "day": bcd_to_dec(data[4]),
            "month": bcd_to_dec(data[5]),
            "year": bcd_to_dec(data[6]) + 2000
        }
    except Exception as e:
        return f"RTC Hatası: {e}"


def read_gps(port="/dev/serial0", baudrate=9600):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        while True:
            line = ser.readline().decode('ascii', errors='replace')
            if line.startswith('$GPGGA') or line.startswith('$GPRMC'):
                try:
                    msg = pynmea2.parse(line)
                    if hasattr(msg, 'latitude') and hasattr(msg, 'longitude'):
                        return {"latitude": msg.latitude, "longitude": msg.longitude}
                except pynmea2.ParseError:
                    continue
    except Exception as e:
        return f"GPS Hatası: {e}"


def read_mpu6050():
    try:
        sensor = mpu6050(0x69)
        return {
            "accel": sensor.get_accel_data(),
            "gyro": sensor.get_gyro_data()
        }
    except Exception as e:
        return f"MPU6050 Hatası: {e}"

if __name__ == "__main__":
    print("### ADS1115 Voltaj Okumaları ###")
    for ch in ["A0", "A1", "A2", "A3"]:
        print(f"{ch}: {read_ads1115(ch)} V")

    print("\n### BMP180 Ölçümleri ###")
    bmp = read_bmp180()
    if isinstance(bmp, dict):
        print(f"Sıcaklık: {bmp['temperature']} °C")
        print(f"Basınç: {bmp['pressure']} Pa")
        print(f"İrtifa: {bmp['altitude']} m")
    else:
        print(bmp)

    print("\n### RTC Saati ###")
    rtc = read_rtc_time()
    if isinstance(rtc, dict):
        print(f"{rtc['hour']:02}:{rtc['minute']:02}:{rtc['second']:02} {rtc['day']:02}/{rtc['month']:02}/{rtc['year']}")
    else:
        print(rtc)

    print("\n### GPS Konumu ###")
    gps = read_gps()
    print(gps)

    print("\n### MPU6050 Verileri ###")
    mpu = read_mpu6050()
    if isinstance(mpu, dict):
        print("Accelerometer:", mpu["accel"])
        print("Gyroscope:", mpu["gyro"])
    else:
        print(mpu)

    time.sleep(1)