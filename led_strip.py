import pigpio
import time
import colorsys

# Set up the pigpio library.
pi = pigpio.pi()

# Define the pins.
green_pin =16
blue_pin = 21
red_pin =20

# Turn off all the pins
pi.set_PWM_dutycycle(green_pin, 0)
pi.set_PWM_dutycycle(blue_pin, 0)
pi.set_PWM_dutycycle(red_pin, 0)

try:

    print("Press Ctrl-C to finish")

    # Set each pin to max in turn - make sure connected correctly
    # Turn green on 100% for a couple of seconds and the off,
    pi.set_PWM_dutycycle(green_pin, 255)
    print("Green? 100%")
    time.sleep(3)
    pi.set_PWM_dutycycle(green_pin, int(255/10))
    print("Green? 10%")
    time.sleep(3)
    pi.set_PWM_dutycycle(green_pin, 0)

    pi.set_PWM_dutycycle(red_pin, 255)
    print("Red?")
    time.sleep(3)
    pi.set_PWM_dutycycle(red_pin, int(255/10))
    print("Red? 10%")
    time.sleep(3)
    pi.set_PWM_dutycycle(red_pin, 0)

    pi.set_PWM_dutycycle(blue_pin, 255)
    print("Blue? 100%")
    time.sleep(3)
    pi.set_PWM_dutycycle(blue_pin, int(255)/10)
    print("Blue? 10%")
    time.sleep(3)
    pi.set_PWM_dutycycle(blue_pin, 0)

    # Keep cycling through various colours - assume the user will press Control-C to finish.
    while True:

        # Cycle through the top ends of value and saturation and through the different colours
        for value in range (75, 100):

            for saturation in range (75,100):

                for hue in range (0, 100):
                    [r, g, b] = colorsys.hsv_to_rgb(hue/100.0, saturation/100.0,  value/100.0)
                    print(hue, saturation, value, r * 255, g * 255, b * 255)

                    pi.set_PWM_dutycycle(green_pin, g * 255)
                    pi.set_PWM_dutycycle(blue_pin, b * 255)
                    pi.set_PWM_dutycycle(red_pin, r *255)

                    time.sleep(0.01)

except KeyboardInterrupt:
    print("Control-C received")

# Clean up to finish -important to turn pins off.
finally:
    pi.set_PWM_dutycycle(green_pin, 0)
    pi.set_PWM_dutycycle(blue_pin, 0)
    pi.set_PWM_dutycycle(red_pin, 0)
    pi.stop()
