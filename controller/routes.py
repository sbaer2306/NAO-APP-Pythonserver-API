from flask import Blueprint, request, jsonify

from move.motions import *

# Create a new Flask Blueprint for your robot controller routes
robot_controller = Blueprint('robot_controller', __name__)

from config.config import *
from move.motions import *
from audio.audio import *
from vision.vision import *
from behavior.behavior import *
@robot_controller.route('/')
def index():
    return "Hello, World!"
#Basic-Config Routes
@robot_controller.route('/api/connect', methods=['POST'])
def connect_route():
    return connect(request)
@robot_controller.route('/api/config/temperature', methods=['GET'])
def get_temperature_route():
    return get_temperature()
@robot_controller.route('/api/config/battery', methods=['GET'])
def get_battery_route():
    return get_battery()
#Audio-Routes
@robot_controller.route('/api/audio/volume', methods=['GET'])
def get_volume_route():
    return get_volume()
@robot_controller.route('/api/audio/volume', methods=['POST'])
def set_volume_route():
    return set_volume(request)
@robot_controller.route('/api/audio/language', methods=['GET'])
def get_language_route():
    return get_language()
@robot_controller.route('/api/audio/language', methods=['POST'])
def set_language_route():
    return set_language(request)
@robot_controller.route('/api/audio/voice', methods=['GET'])
def get_voice_route():
    return get_voices()
@robot_controller.route('/api/audio/voice', methods=['POST'])
def set_voice_route():
    return set_voice(request)
@robot_controller.route('/api/audio/tts', methods=['POST'])
def tts_route():
    return tts(request)
#Movement
@robot_controller.route('/api/move/posture', methods=['POST'])
def move_posture_route():
    return move_posture(request)

@robot_controller.route('/api/move/movement', methods=['POST'])
def movement_route():
    return move_movement(request)
"""@robot_controller.route('/api/move/forward', methods=['POST'])
def move_forward_route():
    return move_forward()

@robot_controller.route('/api/move/backward', methods=['POST'])
def move_backward_route():
    return move_backward()

@robot_controller.route('/api/move/turn_left', methods=['POST'])
def turn_left_route():
    return turn_left()

@robot_controller.route('/api/move/turn_right', methods=['POST'])
def turn_right_route():
    return turn_right()
"""
##vision
@robot_controller.route('/api/vision/brightness', methods=['GET'])
def get_brightness_route():
    return get_brightness()
@robot_controller.route('/api/vision/brightness', methods=['POST'])
def set_brightness_route():
    return set_brightness(request)
#extra
@robot_controller.route('/api/behavior/do_taj_chi', methods=['POST'])
def do_taj_chi_route():
    return do_taj_chi()
@robot_controller.route('/api/behavior/stop_taj_chi', methods=['POST'])
def stop_taj_chi_route():
    return stop_taj_chi()