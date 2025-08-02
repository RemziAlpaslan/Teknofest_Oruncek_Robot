import smbus2
import time

DS1307_ADDRESS = 0x68

def dec_to_bcd(val):
    return (val // 10 * 16) + (val % 10)

def bcd_to_dec(val):
    return (val // 16 * 10) + (val % 16)

def read_time(bus):
    data = bus.read_i2c_block_data(DS1307_ADDRESS, 0x00, 7)
    second = bcd_to_dec(data[0] & 0x7F)
    minute = bcd_to_dec(data[1])
    hour = bcd_to_dec(data[2])
    day = bcd_to_dec(data[4])
    month = bcd_to_dec(data[5])
    year = bcd_to_dec(data[6]) + 2000
    print(f"RTC saati: {hour:02}:{minute:02}:{second:02} {day:02}/{month:02}/{year}")

def write_time(bus):
    now = time.localtime()
    data = [
        dec_to_bcd(now.tm_sec),
        dec_to_bcd(now.tm_min),
        dec_to_bcd(now.tm_hour),
        dec_to_bcd(now.tm_wday),
        dec_to_bcd(now.tm_mday),
        dec_to_bcd(now.tm_mon),
        dec_to_bcd(now.tm_year - 2000)
    ]
    bus.write_i2c_block_data(DS1307_ADDRESS, 0x00, data)
    print("RTC saati güncellendi.")

if __name__ == "__main__":
    bus = smbus2.SMBus(1)
    read_time(bus)

    cevap = input("Raspberry Pi saatini RTC'ye yazmak için 'e' tuşlayın: ").strip().lower()
    if cevap == 'e':
        write_time(bus)
