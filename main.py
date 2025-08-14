import time
import board
import adafruit_dht

# ===== 設定部分 =====
# 利用するGPIO番号（BCM番号）
GPIO_NUM = 18        # 例: GPIO4 → 物理ピン7
SENSOR_TYPE = adafruit_dht.DHT22  # DHT11 の場合は adafruit_dht.DHT11
# ===================

# board モジュールの属性名は D4, D17 のような形式
gpio_attr = f"D{GPIO_NUM}"
dht = SENSOR_TYPE(getattr(board, gpio_attr), use_pulseio=False)

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        if temperature is not None and humidity is not None:
            print(f"Temp: {temperature:.1f} °C, Humidity: {humidity:.1f} %")
        else:
            print("Read failed, retrying...")
    except RuntimeError as e:
        print("Retry:", e)  # 読み取り失敗はよくあるのでリトライ
    time.sleep(2)
