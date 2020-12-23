from flask import Flask,session
import configparser
from composant import Led

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('app.ini')

GPIO_PIN = int(config['DEFAULT']['gpio_pin'])
TWINKLE_TEMPO = float(config['DEFAULT']['twinkle_tempo'])

led  = Led(GPIO_PIN)

@app.route('/')
def hello():
    return { 'message' : 'Hello' }

@app.route('/api/light/on')
def light_on():
    if led.status == led.STOPPED or led.status is None :
        print('Start')
        led.start(TWINKLE_TEMPO)
    return { 'status' : led.status }

@app.route('/api/light/off')
def light_off():
    if led.status == led.STARTED :
        print('Stop')
        led.stop()
    return { 'status' : led.status }

@app.route('/api/light/status')
def light_status():
    return { 'status' : led.status }

if __name__ == "__main__":
    app.run()

