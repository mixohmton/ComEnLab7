import drivers
import RPi.GPIO as GPIO
from time import sleep

SW1 = 27
SW2 = 17

display = drivers.Lcd()
display.lcd_clear()

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

messages = [("TON", "1165"), ("mix", "1165"), ("ohm", "1165")]
current_message_index = 0  # Initialize the message index
stop_program = False  # Flag to indicate whether the program should stop

def switch_pressed(channel):
    global current_message_index, stop_program
    if channel == SW1:
        current_message_index = (current_message_index + 1) % len(messages)
        message = messages[current_message_index]
        display.lcd_clear()
        display.lcd_display_string(message[0], 1)
        display.lcd_display_string(message[1], 2)
    elif channel == SW2:
        print("Writing to LCD !!!")
        display.lcd_display_string("end", 1)
        display.lcd_display_string("Hello World", 2)
        stop_program = True

GPIO.add_event_detect(SW1, GPIO.FALLING, callback=switch_pressed, bouncetime=200)
GPIO.add_event_detect(SW2, GPIO.FALLING, callback=switch_pressed, bouncetime=200)

try:
    while not stop_program:
        print("Waiting for button press...")
        sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    display.lcd_clear()
    print("\nBye...")
