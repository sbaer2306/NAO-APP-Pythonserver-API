from flask import jsonify
from robot_controller.config import NAO_PORT,NAO_IP_ADDRESS
from naoqi import ALProxy

def connect(request):
    NAO_IP_ADDRESS = request.json.get('ip_address')
    NAO_PORT = request.json.get('port')
    try:
        log = ALProxy("ALLogger", NAO_IP_ADDRESS, NAO_PORT)
        log.info("python", "Hello from NAO")
        return jsonify({'message': 'Successfully connected', 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to connect', 'return_code': 500}), 500

def get_temperature():
    try:
        bodyTemperatureProxy = ALProxy("ALBodyTemperature",  NAO_IP_ADDRESS, NAO_PORT)
        level = str(bodyTemperatureProxy.getTemperatureDiagnosis())
        return jsonify({"temperature": level}), 200
    except:
        return jsonify({'message': 'Failed to get temperature', 'return_code': 500}), 500
def get_battery():
    try:
        batteryProxy = ALProxy("ALBattery", NAO_IP_ADDRESS, NAO_PORT)
        level = str(batteryProxy.getBatteryCharge())
        return jsonify({"battery": level}), 200
    except:
        return jsonify({'message': 'Failed to get battery info', 'return_code': 500}), 500


