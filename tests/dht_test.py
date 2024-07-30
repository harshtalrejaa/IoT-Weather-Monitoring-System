#project by ishan somani and harshal talreja

import Adafruit_DHT
import time
# Set sensor type and GPIO pin
sensor = Adafruit_DHT.DHT11
pin = 4

# Get temperature and humidity values
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

while True:
    if humidity is not None and temperature is not None:
        print('Temperature: {0:0.1f}°C'.format(temperature))
        print('Humidity: {0:0.1f}%'.format(humidity))
    else:
        print('Failed to retrieve data from sensor')
        
    time.sleep(2)
