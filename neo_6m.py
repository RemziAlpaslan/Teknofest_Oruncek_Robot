import serial
import pynmea2

"""
pip install pyserial pynmea2 --break-system-packages
"""


def read_gps(port="/dev/serial0", baudrate=9600):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        while True:
            line = ser.readline().decode('ascii', errors='replace')
            if line.startswith('$GPGGA') or line.startswith('$GPRMC'):
                try:
                    msg = pynmea2.parse(line)
                    if hasattr(msg, 'latitude') and hasattr(msg, 'longitude'):
                        print(f"Latitude: {msg.latitude}, Longitude: {msg.longitude}")
                        break
                except pynmea2.ParseError as e:
                    print(f"Parse hatası: {e}")
    except Exception as e:
        print(f"GPS okuma hatası: {e}")

if __name__ == "__main__":
    read_gps()
