import RPi.GPIO as GPIO
import time
import os

# Watermeter stand (wordt alleen initieel gebruikt als er geen bestand meterstand_water.txt is)
global Counter
Counter = 0

# File path for the meterstand_water.txt
file_path = "/homeassistant/www/meterstand_water.txt"

# Function to read and update the counter value
def update_counter_file(counter):
    with open(file_path, "w") as file:
        file.write(counter)

# Function to handle the interrupt event
def interrupt_callback(channel):
    time.sleep(0.05)  # Need to filter out the false positive of some power fluctuation
    if GPIO.input(channel) == 0:
        return

    # Increase the counter by 0.5 liter (assuming a divider of 10 on the water meter)
    global Counter
    Counter += 1

    # Write the updated counter value to the file
    update_counter_file(Counter)


try:
    GPIO.setmode(GPIO.BOARD)
    # Set GPIO 40 (Pin 40) as input with a pull-down resistor
    GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Check if the meterstand_water.txt file exists and read the counter value from it
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.readline()
            _, _, Counter = content.split()
            Counter = int(Counter)
    else:
        # If the file doesn't exist, create it and initialize the counter
        update_counter_file(Counter)

    # Add event detection for rising edge on GPIO 40, calling the interrupt_callback function
    GPIO.add_event_detect(40, GPIO.RISING, callback=interrupt_callback, bouncetime=200)

    while True:
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()



