from pyA20.gpio import gpio
from pyA20.gpio import port

import dht
import time

# initialize GPIO
DHT22_PIN = port.PA13
DHT11_PIN = port.PA6 # PWM port
gpio.init()


#DHT22_instance = dht.DHT22(pin=DHT22_PIN)
DHT11_instance = dht.DHT11(pin=DHT11_PIN)

def DHT22_print_data(DHT22_result):
    if DHT22_result.is_valid():
        print 'Temperature: {}, Humidity: {}'.format(DHT22_result.temperature, DHT22_result.humidity)
    else:
        DHT22_read_sensor()

def DHT22_read_sensor():
    DHT22_result = DHT22_instance.read()
    DHT22_print_data(DHT22_result)

def DHT11_print_data(DHT11_result):
    if DHT11_result.is_valid():
        print 'Temperature: {}, Humidity: {}'.format(DHT11_result.temperature, DHT11_result.humidity)
    else:
        print 'UNKNOWN error: ' + str(DHT11_result.error_code)
        DHT11_read_sensor() # in case of error just reread port (fixme - stackoverflow?)

def DHT11_read_sensor():
    DHT11_result = DHT11_instance.read()
    DHT11_print_data(DHT11_result)

if __name__ == '__main__':
#    DHT22_read_sensor()

    while True:
        time.sleep(2)
        DHT11_read_sensor()
