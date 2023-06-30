from flask import jsonify

from robot_controller import NAO_IP_ADDRESS,NAO_PORT
from naoqi import ALProxy


def get_volume():
    try:
        audioDeviceProxy = ALProxy("ALAudioDevice", NAO_IP_ADDRESS, NAO_PORT)
        level = int(audioDeviceProxy.getOutputVolume())
        return jsonify({"volume": level, 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to set volume','cause': str(e), 'return_code': 500}), 500
def set_volume(request):
    try:
        vol = request.json.get('volume')
        if vol is None:
            return jsonify({'error': 'Volume parameter is not set'}), 400

        vol = int(vol)
        if 0 <= vol <= 100:
            audioDeviceProxy = ALProxy("ALAudioDevice", NAO_IP_ADDRESS, NAO_PORT)
            audioDeviceProxy.setOutputVolume(vol)
            tts_proxy = ALProxy("ALTextToSpeech", NAO_IP_ADDRESS, NAO_PORT)
            tts_proxy.say("Volumne level changed to" + str(vol))
            return jsonify({'message': 'Successfully set volume', 'return_code': 200}), 200
        else:
            return jsonify({'error': 'Volume out of range [0, 100]'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid volume value'}), 400
    except Exception as e:
        return jsonify({'message': 'Failed to set volume', 'cause': str(e), 'return_code': 500}), 500

def get_language():
    try:
        tts = ALProxy('ALTextToSpeech', NAO_IP_ADDRESS, NAO_PORT)
        language=tts.getAvailableLanguages()
        return jsonify({'language': language, 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to get language','cause': str(e), 'return_code': 500}), 500
def set_language(request):
    try:
        tts = ALProxy("ALTextToSpeech", NAO_IP_ADDRESS, NAO_PORT)
        language = str(request.json.get('language'))
        tts.setLanguage(language)
        tts.say("Language changed to" + language)
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
        if voice is None:
            raise ValueError("Voice parameter is missing")

        voice = str(voice)
        tts_proxy.setVoice(voice)
        tts_proxy.say("Voice changed to " + voice)
        return jsonify({'message': 'Successfully set voice', 'return_code': 200}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve), 'return_code': 400}), 400
    except Exception as e:
        return jsonify({'message': 'Failed to set voice', 'cause': str(e), 'return_code': 500}), 500


def tts(request):
    try:
        tts = ALProxy('ALTextToSpeech', NAO_IP_ADDRESS, NAO_PORT)
        message = request.json.get('text')
        if message is None:
            raise ValueError("Text parameter is missing")

        message = str(message)
        tts.say(message)
        return jsonify({'message': 'Successfully used tts', 'return_code': 200}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve), 'return_code': 400}), 400
    except Exception as e:
        return jsonify({'message': 'Failed to use tts', 'cause': str(e), 'return_code': 500}), 500



