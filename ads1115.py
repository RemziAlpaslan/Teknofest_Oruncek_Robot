import time
import board
# board kütüphaneyi indirmek için terminale: pip install board --break-system-packages yazmalısınız.
import busio
# busio kütüphaneyi indirmek için terminale:  pip install board --break-system-packages yazmalısınız.
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
# adafruit_ads1x15.ads1115 kütüphaneyi indirmek için terminale: pip install adafruit-circuitpython-ads1x15 --break-system-packages yazmalısınız.



def ads1115(channel):
    try:
        # I2C bağlantısını oluştur
        i2c = busio.I2C(board.SCL, board.SDA)

        # ADS1115 nesnesini oluştur
        ads = ADS.ADS1115(i2c)

        # Kanal seçimi
        channels = {
            "A0": ADS.P0,
            "A1": ADS.P1,
            "A2": ADS.P2,
            "A3": ADS.P3
        }

        if channel not in channels:
            return "Hata: Geçersiz kanal seçimi! Lütfen 'A0', 'A1', 'A2' veya 'A3' girin."

        # Seçilen kanaldaki veriyi oku
        chan = AnalogIn(ads, channels[channel])
        return chan.voltage

    except Exception as e:
        return f"Hata oluştu: {e}"

# Örnek kullanım
print(ads1115("A0"))
print(ads1115("A1"))
print(ads1115("A2"))
print(ads1115("A3"))
