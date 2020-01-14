from machine import Pin, PWM


class CarCfg:

    FRONT_DIRECTION = Pin(2, Pin.OUT)
    FRONT_PWM = PWM(Pin(4))
    REAR_DIRECTION = Pin(0, Pin.OUT)
    REAR_PWM = PWM(Pin(5))
    PWM_FREQ = 500


