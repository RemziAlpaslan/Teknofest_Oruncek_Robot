from time import sleep
from adafruit_servokit import ServoKit
# adafruit_servokit kütüphaneyi indirmek için terminale: pip install adafruit-circuitpython-servokit --break-system-packages yazmalısınız.

def set_servo_angle(channel, angle):
    """
    Belirtilen kanala bağlı servo motorun açısını ayarlar.
    :param channel: Servo motorun bağlı olduğu kanal (0-15)
    :param angle: Servo motorun gitmesini istediğin açı (0-180 derece)
    """
    try:
        # PCA9685 modülü 16 kanal destekliyor, bu yüzden 16 olarak ayarlıyoruz.
        kit = ServoKit(channels=16)
        
        if 0 <= channel <= 15 and 0 <= angle <= 180:
            kit.servo[channel].angle = angle
            print(f"Servo {channel} açısı {angle}° olarak ayarlandı.")
        else:
            print("Hata: Kanal 0-15, açı ise 0-180 arasında olmalıdır.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Örnek kullanım: Servo motoru belirli açılara hareket ettir
set_servo_angle(0, 175)
sleep(1)
set_servo_angle(0, 45)
sleep(1)
set_servo_angle(0, 90)  # 90° orta konuma getir
sleep(1)
set_servo_angle(0, 0)   # En sola getir
sleep(1)
