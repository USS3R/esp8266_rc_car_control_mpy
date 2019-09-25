import RPi.GPIO as GPIO  # sudo apt-get install python-rpi.gpio


class Driver:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.R_EN = 21
        self.L_EN = 22
        self.RPWM = 23
        self.LPWM = 24
        GPIO.setup(self.R_EN, GPIO.OUT)
        GPIO.setup(self.RPWM, GPIO.OUT)
        GPIO.setup(self.L_EN, GPIO.OUT)
        GPIO.setup(self.LPWM, GPIO.OUT)
        GPIO.output(self.R_EN, True)
        GPIO.output(self.L_EN, True)
        self.pwm_r = GPIO.PWM(self.RPWM, 50)
        self.pwm_l = GPIO.PWM(self.LPWM, 50)
        self.pwm_r.start(0)
        self.pwm_l.start(0)

    def stop(self):
        self.pwm_r.ChangeDutyCycle(0)
        self.pwm_l.ChangeDutyCycle(0)
        GPIO.output(self.RPWM, False)
        GPIO.output(self.LPWM, False)

    def forward(self, pwm_dc):
        GPIO.output(self.LPWM, False)
        GPIO.output(self.RPWM, True)
        self.pwm_l.ChangeDutyCycle(0)
        self.pwm_r.ChangeDutyCycle(pwm_dc)

    def backward(self, pwm_dc):
        GPIO.output(self.RPWM, False)
        GPIO.output(self.LPWM, True)
        self.pwm_r.ChangeDutyCycle(0)
        self.pwm_l.ChangeDutyCycle(pwm_dc)

    def cleanup(self):
        self.pwm_r.ChangeDutyCycle(0)
        self.pwm_l.ChangeDutyCycle(0)
        GPIO.output(self.RPWM, False)
        GPIO.output(self.LPWM, False)
        GPIO.cleanup()


