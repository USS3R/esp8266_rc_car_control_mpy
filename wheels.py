import machine


class Wheels:

    def __init__(self, machine):
        self.machine = machine
        self.FRONT_WHEELS_DIRECTION = machine.Pin(2, machine.Pin.OUT)
        self.FRONT_PWM = machine.PWM(machine.Pin(4))
        self.REAR_WHEELS_DIRECTION = machine.Pin(0, machine.Pin.OUT)
        self.REAR_PWM = machine.PWM(machine.Pin(5))
        self.FRONT_WHEELS_DIRECTION.value(0)
        self.REAR_WHEELS_DIRECTION.value(0)
        self.FRONT_PWM.duty(0)
        self.REAR_PWM.duty(0)

    def stop(self):
        self.FRONT_WHEELS_DIRECTION.value(0)
        self.REAR_WHEELS_DIRECTION.value(0)
        self.FRONT_PWM.duty(0)
        self.REAR_PWM.duty(0)

    def fwd(self, pwm_dc, freq=500):
        self.stop()
        self.REAR_WHEELS_DIRECTION.value(0)
        self.REAR_PWM.duty(pwm_dc)
        self.REAR_PWM.freq(freq)

    def rfwd(self, pwm_dc, freq=500):
        self.stop()
        self.FRONT_WHEELS_DIRECTION.value(0)
        self.FRONT_PWM.duty(pwm_dc)
        self.FRONT_PWM.freq(freq)
        self.REAR_WHEELS_DIRECTION.value(0)
        self.REAR_PWM.duty(pwm_dc)
        self.REAR_PWM.freq(freq)

    def lfwd(self, pwm_dc, freq=500):
        self.stop()
        self.FRONT_WHEELS_DIRECTION.value(1)
        self.FRONT_PWM.duty(pwm_dc)
        self.FRONT_PWM.freq(freq)
        self.REAR_WHEELS_DIRECTION.value(0)
        self.REAR_PWM.duty(pwm_dc)
        self.REAR_PWM.freq(freq)

    def bwd(self, pwm_dc, freq=500):
        self.stop()
        self.REAR_WHEELS_DIRECTION.value(1)
        self.REAR_PWM.duty(pwm_dc)
        self.REAR_PWM.freq(freq)

    def rbwd(self, pwm_dc, freq=500):
        self.stop()
        self.FRONT_WHEELS_DIRECTION.value(0)
        self.FRONT_PWM.duty(pwm_dc)
        self.FRONT_PWM.freq(freq)
        self.REAR_WHEELS_DIRECTION.value(1)
        self.REAR_PWM.duty(pwm_dc)
        self.REAR_PWM.freq(freq)

    def lft(self, pwm_dc, freq=500):
        self.stop()
        self.FRONT_WHEELS_DIRECTION.value(0)
        self.FRONT_PWM.duty(pwm_dc)
        self.FRONT_PWM.freq(freq)

    def rght(self, pwm_dc, freq=500):
        self.stop()
        self.FRONT_WHEELS_DIRECTION.value(1)
        self.FRONT_PWM.duty(pwm_dc)
        self.FRONT_PWM.freq(freq)

    def lbwd(self, pwm_dc, freq=300):
        self.stop()
        self.FRONT_WHEELS_DIRECTION.value(1)
        self.FRONT_PWM.duty(pwm_dc)
        self.FRONT_PWM.freq(freq)
        self.REAR_WHEELS_DIRECTION.value(1)
        self.REAR_PWM.duty(pwm_dc)
        self.REAR_PWM.freq(freq)

    def cleanup(self):
        self.stop()
        self.FRONT_PWM.deinit()
        self.REAR_PWM.deinit()
