from flask import jsonify

from robot_controller import NAO_IP_ADDRESS,NAO_PORT
from naoqi import ALProxy


def get_volume():
    try:
        audioDeviceProxy = ALProxy("ALAudioDevice", NAO_IP_ADDRESS, NAO_PORT)
        level = str(audioDeviceProxy.getOutputVolume())
        return jsonify({"volume": level, 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to set volume', 'return_code': 500}), 500
def set_volume(request):
    try:
        vol = int(request.json.get('volume'))
        if ((vol <= 100) and (vol >= 0)):
            audioDeviceProxy = ALProxy("ALAudioDevice", NAO_IP_ADDRESS, NAO_PORT)
            audioDeviceProxy.setOutputVolume(vol)
            return jsonify({'message': 'Successfully set volume ', 'return_code': 200}), 200
        else:
            return jsonify({"error": "Volume out of range [0,100]"}), 400
    except:
        return jsonify({'message': 'Failed to set volume', 'return_code': 500}), 500
def get_language():
    try:
        languageProxy = ALProxy("ALTextToSpeechProxy", NAO_IP_ADDRESS, NAO_PORT)
        language=languageProxy.getLanguage()
        return jsonify({'message': 'Successfully got language','language': language, 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to get language', 'return_code': 500}), 500
def set_language(request):
    try:
        languageProxy = ALProxy("ALDialog", NAO_IP_ADDRESS, NAO_PORT)
        language = str(request.json.get)
        languageProxy.setLanguage(language)
        return jsonify({'message': 'Successfully set language', 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to set language', 'return_code': 500}), 500
def tts(request):
    try:
        tts = ALProxy('ALTextToSpeech', NAO_IP_ADDRESS, NAO_PORT)
        message = request.json.get('text')
        tts.say(message)
        return jsonify({'message': 'Successfully used tts', 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to use tts', 'return_code': 500}), 500

