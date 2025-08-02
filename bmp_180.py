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

def read_bmp180():
    try:
        sensor = BMP085.BMP085(busnum=1)
        
        temperature = sensor.read_temperature()
        pressure = sensor.read_pressure()
        altitude = sensor.read_altitude()
        
        return (temperature, pressure, altitude)
    except Exception as e:
        print("Sensör okuma sırasında hata oluştu:", e)
        return None

# Fonksiyonun test edilmesi
if __name__ == "__main__":
    result = read_bmp180()
    if result:
        temperature, pressure, altitude = result
        print(f"Temp = {temperature:0.2f} *C")
        print(f"Pressure = {pressure:0.2f} Pa")
        print(f"Altitude = {altitude:0.2f} m")
    else:
        print("Sensör verisi alınamadı.")

