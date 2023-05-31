from flask import jsonify
from robot_controller.config import NAO_PORT,NAO_IP_ADDRESS
from naoqi import ALProxy

def do_taj_chi():
    try:
        behavior_proxy = ALProxy("ALBehaviorManager", NAO_IP_ADDRESS, NAO_PORT)
        #TODO: PATH to tajchi
        behavior_module = "path/to/behavior_module.py"
        behavior_name = "taj_chi"
        behavior_proxy.addBehavior(behavior_name, behavior_module)
        behavior_proxy.startBehavior(behavior_name)
        return jsonify({'message': 'Successfully doing taj chi', 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to do taj chi', 'return_code': 500}), 500
def stop_taj_chi():
    try:
        behavior_proxy = ALProxy("ALBehaviorManager", NAO_IP_ADDRESS, NAO_PORT)
        behavior_name = "taj_chi"
        behavior_proxy.startBehavior(behavior_name)
        return jsonify({'message': 'Successfully stopped taj chi', 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to stop taj chi', 'return_code': 500}), 500

