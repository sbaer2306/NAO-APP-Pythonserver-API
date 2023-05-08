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

def move_movement(request):
    # Send command to NAO-Robot to move forward
    try:
        motionProxy = ALProxy("ALMotion", NAO_IP_ADDRESS, NAO_PORT)

        StiffnessOn(motionProxy)

        enableArmsInWalkAlgorithm = bool(request.json.get("enableArmsInWalkAlgorithm"))

        motionProxy.setWalkArmsEnabled(enableArmsInWalkAlgorithm, enableArmsInWalkAlgorithm)
        motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])

        xForwardBackward = float(request.json.get("xCoordinate"))
        yLeftRight = float(request.json.get("yCoordinate"))
        tRotation = float(request.json.get("tCoordinate"))
        speed = float(request.json.get("speed"))

        motionProxy.setWalkTargetVelocity(xForwardBackward, yLeftRight, tRotation, speed)
    except:
        return jsonify({'message': 'Failed to move', 'return_code': 500}), 500

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

