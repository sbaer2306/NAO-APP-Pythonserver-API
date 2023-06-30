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
            raise ValueError("Missing volume parameter")

        vol = int(vol)
        if 0 <= vol <= 100:
            audioDeviceProxy = ALProxy("ALAudioDevice", NAO_IP_ADDRESS, NAO_PORT)
            audioDeviceProxy.setOutputVolume(vol)
            tts_proxy = ALProxy("ALTextToSpeech", NAO_IP_ADDRESS, NAO_PORT)
            tts_proxy.say("Volume level changed to" + str(vol))
            return jsonify({'message': 'Successfully set volume', 'return_code': 200}), 200
        else:
            raise ValueError("Volume out of range (0-100)")
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

        if not language:
            raise ValueError("Language parameter missing")

        tts.setLanguage(language)
        tts.say("Language changed to" + language)
        return jsonify({'message': 'Successfully set language', 'return_code': 200}), 200
    except ValueError as ve:
        return jsonify({'message': 'Invalid language value', 'cause': str(ve), 'return_code': 400}), 400
    except Exception as e:
        return jsonify({'message': 'Failed to set language', 'cause': str(e), 'return_code': 500}), 500


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
        voice = str(request.json.get('voice'))

        if not voice:
            raise ValueError("Voice parameter missing")

        tts_proxy.setVoice(voice)
        tts_proxy.say("Voice changed to" +voice)
        return jsonify({'message': 'Successfully set voice', 'return_code': 200}), 200
    except ValueError as ve:
        return jsonify({'message': 'Invalid voice value', 'cause': str(ve), 'return_code': 400}), 400
    except Exception as e:
        return jsonify({'message': 'Failed to set voice','cause': str(e), 'return_code': 500}), 500
def tts(request):
    try:
        tts = ALProxy('ALTextToSpeech', NAO_IP_ADDRESS, NAO_PORT)
        message = str(request.json.get('text'))

        if not message:
            raise ValueError("Text parameter missing")

        tts.say(message)
        return jsonify({'message': 'Successfully used tts', 'return_code': 200}), 200
    except ValueError as ve:
        return jsonify({'message': 'Invalid text value', 'cause': str(ve), 'return_code': 400}), 400
    except Exception as e:
        return jsonify({'message': 'Failed to use tts','cause': str(e), 'return_code': 500}), 500

