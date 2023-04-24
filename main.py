import Adafruit_DHT
import RPi.GPIO as GPIO
from rpi_lcd import LCD
from signal import signal, SIGTERM, SIGHUP, pause
import requests
import time

# Set the URL of the ThingSpeak API
url = "https://api.thingspeak.com/update"

# Set sensor type and GPIO lpin for DHT11
dht_sensor = Adafruit_DHT.DHT11
dht_pin = 4

# Set GPIO pin for rain sensor
rain_pin = 17

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set rain sensor pin as input with pull-up resistor
GPIO.setup(rain_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

lcd = LCD()

# Get temperature and humidity values
humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)

# Get rain sensor value
rain_value = GPIO.input(rain_pin)

print (temperature)
print(humidity)
# Print temperature, humidity, and rain sensor values
if humidity is not None and temperature is not None:
    print('Temperature: {0:0.1f}°C'.format(temperature))
    print('Humidity: {0:0.1f}%'.format(humidity))
else:
    print('Failed to retrieve data from DHT11 sensor')

print('Rain sensor value: {0}'.format(rain_value))
def safe_exit(signum, frame):
    exit(1)
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text(f'T:{temperature}C H: {humidity}', 1)
    lcd.text(f'Rain: {rain_value}', 2)
    #pause()
    time.sleep(10)
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()


# Set the parameters of the request
params = {
    "api_key": "INSERT_API_KEY",
    "field1": temperature,
    "field2": humidity,
    "field3": rain_value
}
# Send the request to ThingSpeak
response = requests.get(url, params=params)
print("Data Sent Successfully!")
# Print the response from ThingSpeak
print(response.content)