import cv2
from flask import jsonify
from robot_controller.config import NAO_PORT,NAO_IP_ADDRESS
from naoqi import ALProxy

def get_brightness():
    try:
        videoProxy = ALProxy("ALVideoDevice", NAO_IP_ADDRESS,NAO_PORT)
        brightness=videoProxy.getParameter(0,0)
        return jsonify({ 'brightness': brightness, 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to get brightness','cause': str(e), 'return_code': 500}), 500
def set_brightness(request):
    try:
        brightness = int(request.json.get('brightness'))
        print(brightness)
        videoProxy = ALProxy("ALVideoDevice", NAO_IP_ADDRESS,NAO_PORT)
        videoProxy.setParameter(0, 0, brightness)
        return jsonify({'message': 'Successfully set brightness', 'brightness': brightness, 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to set brightness','cause': str(e), 'return_code': 500}), 500



