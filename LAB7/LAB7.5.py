import RPi.GPIO as GPIO
import time
import drivers

SW1 = 17
SW2 = 27
lcd_position = 0


display = drivers.Lcd()
display.lcd_clear()


MAX_WIDTH = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(SW1) == GPIO.LOW:
            if lcd_position < MAX_WIDTH:
                lcd_position += 1
            display.lcd_clear()
            display.lcd_display_string(" " * lcd_position + "Lab7 ", 1)
            print("1")
            time.sleep(0.2)
        elif GPIO.input(SW2) == GPIO.LOW:
            lcd_position -= 1
            if lcd_position < 0:
                lcd_position = 0
            display.lcd_clear()
            display.lcd_display_string(" " * lcd_position + "Lab7 ", 1)
            print("2")
            time.sleep(0.2)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye...")
