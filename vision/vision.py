from .vision import *
from flask import jsonify
from robot_controller.config import NAO_PORT,NAO_IP_ADDRESS
from naoqi import ALProxy

def get_brightness():
    try:
        videoProxy = ALProxy("ALVideoDeviceProxy", NAO_IP_ADDRESS,NAO_PORT)
        brightness=videoProxy.getParameter(0,'Brightness')
        return jsonify({'message': 'Successfully got brightness', 'brightness': brightness, 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to get brightness', 'return_code': 500}), 500
def set_brightness(request):
    try:
        brightness = request.json.get('brightness')
        videoProxy = ALProxy("ALVideoDeviceProxy", NAO_IP_ADDRESS,NAO_PORT)
        videoProxy.setParameter(0,'Brightness',brightness)
        return jsonify({'message': 'Successfully set brightness', 'brightness': brightness, 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to set brightness', 'return_code': 500}), 500

