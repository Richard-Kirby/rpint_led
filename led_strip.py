import pigpio
import time
import colorsys


pi = pigpio.pi()

green_pin =16
blue_pin = 21
red_pin =20

low_pwm =50
high_pwm =255

pi.set_PWM_dutycycle(green_pin, 0)

pi.set_PWM_dutycycle(blue_pin, 0)
pi.set_PWM_dutycycle(red_pin, 0)

try:
    while True:
        for value in range (75, 100):

            for saturation in range (75,100):

                for hue in range (0, 100):
                    [r, g, b] = colorsys.hsv_to_rgb(hue/100.0, saturation/100.0,  value/100.0)
                    print(hue, saturation, value, r * 255, g * 255, b * 255)

                    pi.set_PWM_dutycycle(green_pin, g * 255)
                    pi.set_PWM_dutycycle(blue_pin, b * 255)
                    pi.set_PWM_dutycycle(red_pin, r *255)

                    time.sleep(0.3)

finally:
    pi.set_PWM_dutycycle(green_pin, 0)
    pi.set_PWM_dutycycle(blue_pin, 0)
    pi.set_PWM_dutycycle(red_pin, 0)
