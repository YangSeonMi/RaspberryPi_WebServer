from flask import Flask, request, render_template, jsonify
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)

@app.route('/api/angle', methods=['POST'])
def control_servo():
    data = request.get_json()
    angle = data.get('angle')  # POST 요청에서 'angle' 값을 가져옴
    if angle is not None:
        setAngle(int(angle))  # 서보 모터 각도 설정
        return jsonify({'message': 'angle set to {}'.format(angle)})
    else:
        return jsonify({'message': 'fail! check your parameter'})
