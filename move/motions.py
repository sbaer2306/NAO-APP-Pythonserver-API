from flask import jsonify
from robot_controller.config import NAO_IP_ADDRESS,NAO_PORT
from naoqi import ALProxy

def move_posture(request):
    try:
        postureProxy = ALProxy("ALRobotPosture", NAO_IP_ADDRESS, NAO_PORT)
        posture = request.json.get("posture")
        speed = request.json.get("speed")

        if posture is None or speed is None:
            raise ValueError("Both posture and speed parameters are required")

        posture = str(posture)
        speed = float(speed)

        postureProxy.goToPosture(posture, speed)

        return jsonify({'message': 'Successfully done posture', 'return_code': 200}), 200
    except ValueError as ve:
        return jsonify({'message': 'Failed to do posture', 'cause': str(ve), 'return_code': 400}), 400
    except Exception as e:
        return jsonify({'message': 'Failed to do posture', 'cause': str(e), 'return_code': 500}), 500

def move_movement(request):
    try:
        postureProxy = ALProxy("ALRobotPosture", NAO_IP_ADDRESS, NAO_PORT)
        postureProxy.goToPosture("StandZero", "1.0")
        motionProxy = ALProxy("ALMotion", NAO_IP_ADDRESS, NAO_PORT)

        StiffnessOn(motionProxy)

        enableArmsInWalkAlgorithm = request.json.get("enableArmsInWalkAlgorithm")
        xCoordinate = request.json.get("xCoordinate")
        yCoordinate = request.json.get("yCoordinate")
        tCoordinate = request.json.get("tCoordinate")
        speed = request.json.get("speed")

        if (
                enableArmsInWalkAlgorithm is None
                or xCoordinate is None
                or yCoordinate is None
                or tCoordinate is None
                or speed is None
        ):
            raise ValueError("All parameters are required")

        enableArmsInWalkAlgorithm = bool(enableArmsInWalkAlgorithm)
        xForwardBackward = float(xCoordinate)
        yLeftRight = float(yCoordinate)
        tRotation = float(tCoordinate)
        speed = float(speed)

        motionProxy.setWalkArmsEnabled(enableArmsInWalkAlgorithm, enableArmsInWalkAlgorithm)
        motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
        motionProxy.setWalkTargetVelocity(xForwardBackward, yLeftRight, tRotation, speed)

        return jsonify({'message': 'Successfully moving', 'return_code': 200}), 200
    except ValueError as ve:
        return jsonify({'message': 'Failed to move', 'cause': str(ve), 'return_code': 400}), 400
    except Exception as e:
        return jsonify({'message': 'Failed to move', 'cause': str(e), 'return_code': 500}), 500


def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

