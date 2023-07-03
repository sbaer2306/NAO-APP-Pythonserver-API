from flask import jsonify
from robot_controller.config import NAO_PORT,NAO_IP_ADDRESS
from naoqi import ALProxy

def do_taj_chi():
    try:
        behavior_proxy = ALProxy("ALBehaviorManager", NAO_IP_ADDRESS, NAO_PORT)
        behavior_proxy.startBehavior('taichi-dance-free')
        return jsonify({'message': 'Successfully doing taj chi', 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to do taj chi', 'return_code': 500}), 500
def stop_taj_chi():
    try:
        behavior_proxy = ALProxy("ALBehaviorManager", NAO_IP_ADDRESS, NAO_PORT)
        behavior_proxy.stopBehavior('taichi-dance-free')
        return jsonify({'message': 'Successfully stopped taj chi', 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to stop taj chi', 'return_code': 500}), 500

