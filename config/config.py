from flask import jsonify
from robot_controller.config import NAO_PORT,NAO_IP_ADDRESS
from naoqi import ALProxy


def connect(request):
    try:
        NAO_IP_ADDRESS = request.json.get('ip_address')
        NAO_PORT = request.json.get('port')

        if NAO_IP_ADDRESS is None or NAO_PORT is None:
            raise ValueError("Both 'ip_address' and 'port' parameters are required")

        tts_proxy = ALProxy("ALTextToSpeech", NAO_IP_ADDRESS, NAO_PORT)
        tts_proxy.say("NAO-APP connected")

        return jsonify({'message': 'Successfully connected', 'return_code': 200}), 200
    except ValueError as ve:
        return jsonify({'message': 'Failed to connect', 'cause': str(ve), 'return_code': 400}), 400
    except Exception as e:
        return jsonify({'message': 'Failed to connect', 'cause': str(e), 'return_code': 500}), 500


def get_temperature():
    try:
        bodyTemperatureProxy = ALProxy('ALBodyTemperature',  NAO_IP_ADDRESS, NAO_PORT)
        level = str(bodyTemperatureProxy.getTemperatureDiagnosis())
        return jsonify({"temperature": level, 'return:code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to get temperature','cause': str(e), 'return_code': 500}), 500
def get_battery():
    try:
        batteryProxy = ALProxy("ALBattery", NAO_IP_ADDRESS, NAO_PORT)
        level = int(batteryProxy.getBatteryCharge())
        return jsonify({"battery": level, 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to get battery info', 'return_code': 500}), 500

def get_wifi_strength():
    try:
        alconnman = ALProxy("ALConnectionManager", NAO_IP_ADDRESS, NAO_PORT)
        alconnman.scan()
        data = alconnman.services()
        strength = data[0][12][1]
        return jsonify({"strength": strength, 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to get wifi strength info','cause': str(e), 'return_code': 500}), 500



