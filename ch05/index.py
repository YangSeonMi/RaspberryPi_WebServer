from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)

def setAngle(angle):
    pwm = GPIO.PWM(16, 50)  # 핀 16, 50Hz
    pwm.start(0)
    duty = angle / 18 + 2
    GPIO.output(16, True)
    pwm.ChangeDutyCycle(duty)
    sleep(0.5)
    GPIO.output(16, False)
    pwm.ChangeDutyCycle(0)
    pwm.stop()

@app.route('/')
def home():
    return reder_template("index.html")

@app.route('/api/angle', methods=['POST'])
def control_servo():
    data = request.get_json()
    angle = data.get('angle')
    if angle is not None:
        setAngle(int(angle))
        return jsonify({'message': f'angle set to {angle}'})
    else:
        return jsonify({'message': 'fail! check your parameter'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
