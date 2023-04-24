
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
lcd = LCD()
def safe_exit(signum, frame):
    exit(1)
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text("Hello World!")
    lcd.text("Have A Good Day!")
    #pause()
    time.sleep(10)
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
