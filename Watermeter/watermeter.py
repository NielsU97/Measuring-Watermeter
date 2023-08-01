import RPi.GPIO as GPIO
import time
import os

# Set GPIO 21 (Pin 40) as Input and activate pull-up resistor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

fn = "/homeassistant/www/meterstand_water.txt"

def read_counter_from_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read().strip()
            if content.isdigit():
                return int(content)
            else:
                return 0
    else:
        with open(filename, "w") as f:
            f.write('0')
        return 0

def write_counter_to_file(filename, counter):
    with open(filename, 'w') as f:
        f.write(str(counter))

# Read the initial counter value from the file
Counter = read_counter_from_file(fn)

# Function callback for interrupt event
def Interrupt(channel):
    time.sleep(0.05)  # Filter out false positives from power fluctuations
    if GPIO.input(40) == 0:
        return

    # Increment the counter
    global Counter
    Counter += 1

    # Write the updated counter value to the file
    write_counter_to_file(fn, Counter)

# Add interrupt event detection, detecting rising edge
GPIO.add_event_detect(40, GPIO.RISING, callback=Interrupt, bouncetime=200)

try:
    while True:
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()