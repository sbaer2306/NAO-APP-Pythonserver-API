from flask import jsonify
from robot_controller.config import NAO_PORT,NAO_IP_ADDRESS
from naoqi import ALProxy
def move_posture(request):
    try:
        postureProxy = ALProxy("ALRobotPosture", NAO_IP_ADDRESS,NAO_PORT)
        postureProxy.goToPosture(request.json.get("posture"), request.json.get("speed"))
        return jsonify({'message': 'Successfully connected', 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to connect', 'return_code': 500}), 500

def move_forward():
    # Send command to NAO-Robot to move forward
    robot.move_forward()
    return 'OK'

def move_backward():
    # Send command to NAO-Robot to move backward
    robot.move_backward()
    return 'OK'

def turn_left():
    # Send command to NAO-Robot to turn left
    robot.turn_left()
    return 'OK'

def turn_right():
    # Send command to NAO-Robot to turn right
    robot.turn_right()
    return 'OK'
