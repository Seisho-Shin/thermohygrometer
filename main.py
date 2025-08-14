import Adafruit_DHT as DHT

#センサータイプを指定
SENSOR_TYPE=DHT.DHT22
#接続したGPIOピンを指定
DHT_GPIO=1

humid,temp = DHT.read_retry(SENSOR_TYPE, DHT_GPIO)