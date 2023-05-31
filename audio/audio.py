from flask import jsonify

from robot_controller import NAO_IP_ADDRESS,NAO_PORT
from naoqi import ALProxy


def get_volume():
    try:
        audioDeviceProxy = ALProxy("ALAudioDevice", NAO_IP_ADDRESS, NAO_PORT)
        level = str(audioDeviceProxy.getOutputVolume())
        return jsonify({"volume": level, 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to set volume','cause': str(e), 'return_code': 500}), 500
def set_volume(request):
    try:
        vol = int(request.json.get('volume'))
        if ((vol <= 100) and (vol >= 0)):
            audioDeviceProxy = ALProxy("ALAudioDevice", NAO_IP_ADDRESS, NAO_PORT)
            audioDeviceProxy.setOutputVolume(vol)
            return jsonify({'message': 'Successfully set volume ', 'return_code': 200}), 200
        else:
            return jsonify({"error": "Volume out of range [0,100]"}), 400
    except Exception as e:
        return jsonify({'message': 'Failed to set volume','cause': str(e), 'return_code': 500}), 500
def get_language():
    try:
        tts = ALProxy('ALTextToSpeech', NAO_IP_ADDRESS, NAO_PORT)
        language=tts.getAvailableLanguages()
        return jsonify({'message': 'Successfully got language','language': language, 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to get language','cause': str(e), 'return_code': 500}), 500
def set_language(request):
    try:
        tts = ALProxy("ALTextToSpeech", NAO_IP_ADDRESS, NAO_PORT)
        language = str(request.json.get('language'))
        tts.setLanguage(language)
        return jsonify({'message': 'Successfully set language', 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to set language','cause': str(e), 'return_code': 500}), 500
def get_voices():
    try:
        tts = ALProxy('ALTextToSpeech', NAO_IP_ADDRESS, NAO_PORT)
        voices = tts.getAvailableVoices()
        return jsonify({'voices': voices, 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to get voices','cause': str(e), 'return_code': 500}), 500
def set_voice(request):
    try:
        tts_proxy = ALProxy("ALTextToSpeech", NAO_IP_ADDRESS, NAO_PORT)
        voice = request.json.get('voice')
        tts_proxy.setVoice(voice)
        tts_proxy.say("Voice changed to" +voice)
        return jsonify({'message': 'Successfully set voice', 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to set voice','cause': str(e), 'return_code': 500}), 500
def tts(request):
    try:
        tts = ALProxy('ALTextToSpeech', NAO_IP_ADDRESS, NAO_PORT)
        message = str(request.json.get('text'))
        tts.say(message)
        return jsonify({'message': 'Successfully used tts', 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to use tts','cause': str(e), 'return_code': 500}), 500

