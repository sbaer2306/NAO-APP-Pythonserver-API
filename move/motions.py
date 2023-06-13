from flask import jsonify
from robot_controller.config import NAO_IP_ADDRESS,NAO_PORT
from naoqi import ALProxy
def move_posture(request):
    try:
        postureProxy = ALProxy("ALRobotPosture", NAO_IP_ADDRESS,NAO_PORT)
        posture = str(request.json.get("posture"))
        speed = float(request.json.get("speed"))
        postureProxy.goToPosture(posture,speed)
        return jsonify({'message': 'Successfully done posture', 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to do posture','cause': str(e), 'return_code': 500}), 500

def move_movement(request):
    # Send command to NAO-Robot to move forward
    try:
        #postureProxy = ALProxy("ALRobotPosture", NAO_IP_ADDRESS, NAO_PORT)
        #posture = str("Stand")
        #speed = float(1.0)
        #postureProxy.goToPosture(posture, speed)
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
        return jsonify(
            {'message': 'Successfully moving', 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to move','cause': str(e), 'return_code': 500}), 500

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

