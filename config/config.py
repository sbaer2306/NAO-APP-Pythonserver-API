from flask import jsonify
from robot_controller.config import NAO_PORT,NAO_IP_ADDRESS
#from naoqi import ALProxy

def connect(request):
    print(request.json)
    NAO_IP_ADDRESS = request.json.get('ip_address')
    NAO_PORT = request.json.get('port')
    try:
        #log = ALProxy("ALLogger", NAO_IP_ADDRESS, NAO_PORT)
        #log.info("python", "Hello from NAO")
        return jsonify({'message': 'Successfully connected', 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to connect', 'return_code': 500}), 500
def get_volume():
    return 'OK'
def set_volume(volume):
    vol = int(volume)
    if ((vol <= 100) and (vol >= 0)):
        # audioDeviceProxy = ALProxy("ALAudioDevice", nao_host, nao_port)
        # audioDeviceProxy.setOutputVolume(vol)
        return jsonify({"volume": vol}), 200
    else:
        return jsonify({"error": "Volume out of range [0,100]"}), 400
