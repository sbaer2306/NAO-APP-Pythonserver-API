from flask import Blueprint, request, jsonify

from move.motions import *

# Create a new Flask Blueprint for your robot controller routes
robot_controller = Blueprint('robot_controller', __name__)

from config.config import *
from move import motions
from audio.audio import *
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
@robot_controller.route('/api/audio/tts', methods=['POST'])
def tts_route():
    return set_language(request)
#Movement
@robot_controller.route('/api/move/posture', methods=['POST'])
def move_posture_route():
    return move_posture(request)
@robot_controller.route('/api/move/forward', methods=['POST'])
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

""""
@app.route('/temperature', methods=['GET'])
def get_temperature_diagnosis():
    logger.debug("get_temperature_diagnosis() called")
    bodyTemperatureProxy = ALProxy("ALBodyTemperature", nao_host, nao_port)
    level = str(bodyTemperatureProxy.getTemperatureDiagnosis())
    return jsonify({"temperature": level}), 200

@app.route('/battery', methods=['GET'])
def get_battery_level():
    logger.debug("get_batteryLevel() called")
    batteryProxy = ALProxy("ALBattery", nao_host, nao_port)
    level = str(batteryProxy.getBatteryCharge())
    return jsonify({"battery": level}), 200

@app.route('/behaviors', methods=['GET'])
def get_behaviors():
    logger.debug("get_behaviors() called")
    managerProxy = ALProxy("ALBehaviorManager", nao_host, nao_port)
    behaviors = managerProxy.getInstalledBehaviors()
    return jsonify({"behaviors": behaviors}), 200

@app.route('/behaviors/start', methods=['POST'])
def start_behavior():
    logger.debug("start_behavior() called")
    if not request.json or not 'behavior' in request.json:
        abort(400)
    behavior = str(request.json['behavior'])
    managerProxy = ALProxy("ALBehaviorManager", nao_host, nao_port)

    if (managerProxy.isBehaviorInstalled(behavior)):
        logger.debug("Behavior "+behavior+" is present on the robot, starting behavior...")
        managerProxy.post.runBehavior(behavior)
        return jsonify({"started": behavior}), 200
    else:
        logger.debug("Behavior "+behavior+" is NOT present on the robot")
        return jsonify({"error": "Behavior not found"}), 404

@app.route('/behaviors/stop', methods=['POST'])
def stop_behavior():
    logger.debug("stop_behavior() called")
    if not request.json or not 'behavior' in request.json:
        abort(400)
    behavior = str(request.json['behavior'])
    managerProxy = ALProxy("ALBehaviorManager", nao_host, nao_port)

    if (managerProxy.isBehaviorRunning(behavior)):
        logger.debug("Behavior "+behavior+" is running on the robot, stopping behavior...")
        managerProxy.stopBehavior(behavior)
        return jsonify({"stopped": behavior}), 200
    else:
        logger.debug("Behavior "+behavior+" is NOT running on the robot")
        return jsonify({"error": "Behavior not running"}), 404

@app.route('/behaviors/stop/all', methods=['GET'])
def stop_behaviors():
    logger.debug("stop_behaviors() called")
    managerProxy = ALProxy("ALBehaviorManager", nao_host, nao_port)
    behaviors = managerProxy.getRunningBehaviors()

    if (len(behaviors) > 0):
        managerProxy.stopAllBehaviors()
        return jsonify({"stopped": behaviors}), 200
    else:
        return jsonify({"error": "No running behaviors"}), 400


@app.route('/say', methods=['POST'])
def say():
    if not request.json or not 'text' in request.json:
        abort(400)
    tts = ALProxy("ALTextToSpeech", nao_host, nao_port)
    tts.say(str(request.json['text']))
    return jsonify({'text': request.json['text']}), 200

@app.route('/ask/<string:question>', methods=['GET'])
def ask(question):
    tts = ALProxy("ALTextToSpeech", nao_host, nao_port)
    tts.say(str(question))
    return jsonify({'question': question}), 200

@app.route('/robots', methods=['GET'])
def get_robots():
    return jsonify({'robots': robots}), 200

@app.route('/robots/<int:robot_id>', methods=['GET'])
def get_robot(robot_id):
    robot = [robot for robot in robots if robot['id'] == robot_id]
    if len(robot) == 0:
        abort(404)
    return jsonify({'robot': robot[0]}), 200
"""