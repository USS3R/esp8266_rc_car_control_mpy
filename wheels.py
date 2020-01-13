from machine import Pin, PWM


class Car:

    def __init__(self):
        self.FRONT_DIRECTION = CarCfg.FRONT_DIRECTION
        self.REAR_DIRECTION = CarCfg.REAR_DIRECTION
        self.FRONT_PWM = CarCfg.FRONT_PWM
        self.REAR_PWM = CarCfg.REAR_PWM
        self.FREQ = CarCfg.PWM_FREQ
        self.FRONT_DIRECTION.value(0)
        self.REAR_DIRECTION.value(0)
        self.FRONT_PWM.duty(0)
        self.REAR_PWM.duty(0)

    def stop(self):
        self.FRONT_DIRECTION.value(0)
        self.REAR_DIRECTION.value(0)
        self.FRONT_PWM.duty(0)
        self.REAR_PWM.duty(0)

    def forward(self, pwm_dc):
        self.stop()
        self.REAR_DIRECTION.value(0)
        self.REAR_PWM.duty(pwm_dc)
        self.REAR_PWM.freq(self.FREQ)

    def forward_right(self, pwm_dc):
        self.stop()
        self.FRONT_DIRECTION.value(0)
        self.FRONT_PWM.duty(pwm_dc)
        self.FRONT_PWM.freq(self.FREQ)
        self.REAR_DIRECTION.value(0)
        self.REAR_PWM.duty(pwm_dc)
        self.REAR_PWM.freq(self.FREQ)

    def forward_left(self, pwm_dc):
        self.stop()
        self.FRONT_DIRECTION.value(1)
        self.FRONT_PWM.duty(pwm_dc)
        self.FRONT_PWM.freq(self.FREQ)
        self.REAR_DIRECTION.value(0)
        self.REAR_PWM.duty(pwm_dc)
        self.REAR_PWM.freq(self.FREQ)

    def backward(self, pwm_dc):
        self.stop()
        self.REAR_DIRECTION.value(1)
        self.REAR_PWM.duty(pwm_dc)
        self.REAR_PWM.freq(self.FREQ)

    def backward_right(self, pwm_dc):
        self.stop()
        self.FRONT_DIRECTION.value(0)
        self.FRONT_PWM.duty(pwm_dc)
        self.FRONT_PWM.freq(self.FREQ)
        self.REAR_DIRECTION.value(1)
        self.REAR_PWM.duty(pwm_dc)
        self.REAR_PWM.freq(self.FREQ)

    def backward_left(self, pwm_dc):
        self.stop()
        self.FRONT_DIRECTION.value(1)
        self.FRONT_PWM.duty(pwm_dc)
        self.FRONT_PWM.freq(self.FREQ)
        self.REAR_DIRECTION.value(1)
        self.REAR_PWM.duty(pwm_dc)
        self.REAR_PWM.freq(self.FREQ)

    def left(self, pwm_dc):
        self.stop()
        self.FRONT_DIRECTION.value(0)
        self.FRONT_PWM.duty(pwm_dc)
        self.FRONT_PWM.freq(self.FREQ)

    def right(self, pwm_dc):
        self.stop()
        self.FRONT_DIRECTION.value(1)
        self.FRONT_PWM.duty(pwm_dc)
        self.FRONT_PWM.freq(self.FREQ)

    def cleanup(self):
        self.stop()
        self.FRONT_PWM.deinit()
        self.REAR_PWM.deinit()

    def skip(self):
        pass
