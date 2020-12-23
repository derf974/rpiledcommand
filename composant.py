from multiprocessing import Process
import RPi.GPIO as GPIO
import time

class Led:

    def __init__(self,pin):
        self.id = None
        self.pin = pin
        self.status = None
        self.STOPPED = "STOPPED"
        self.STARTED = "STARTED"
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT, initial = GPIO.HIGH)


    def start(self,tempo):
        if self.id is None:
            self.id = Process(target=self.twinkle,args=(tempo,) )
            self.id.start()
            print('STATUS : ' + str(self.id))
            if self.id == -1 :
                self.status = self.STOPPED
                return False
            else:
                self.status=self.STARTED
            return True
        return False

    def stop(self):
        if self.id is not None:
            self.id.kill()
            self.id = None
            self.status = self.STOPPED
            GPIO.output(self.pin, GPIO.LOW)
            return True
        return False

    def twinkle(self,tempo):
        while True:
            self.status = self.STARTED
            GPIO.output(self.pin, not GPIO.input(self.pin))
            time.sleep(tempo)
