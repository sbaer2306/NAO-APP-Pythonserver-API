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

        if speed < 0.1 or speed > 1.0:
            raise ValueError("Speed should be between 0.1 and 1.0")

        valid_postures = ["Crouch", "LyingBack", "LyingBelly", "Sit", "SitRelax", "Stand", "StandInit", "StandZero"]
        if posture not in valid_postures:
            raise ValueError("Invalid posture")

        postureProxy.goToPosture(posture, speed)

        return jsonify({'message': 'Successfully done posture', 'return_code': 200}), 200
    except ValueError as ve:
        return jsonify({'message': 'Failed to do posture', 'cause': str(ve), 'return_code': 400}), 400
    except Exception as e:
        return jsonify({'message': 'Failed to do posture', 'cause': str(e), 'return_code': 500}), 500

def move_movement(request):
    try:
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

        if (
                xForwardBackward < -1.0 or xForwardBackward > 1.0
                or yLeftRight < -1.0 or yLeftRight > 1.0
                or tRotation < -1.0 or tRotation > 1.0
        ):
            raise ValueError("Coordinates should be between -1.0 and 1.0")

        if speed < 0.0 or speed > 1.0:
            raise ValueError("Speed should be between 0.0 and 1.0")

        not_moving = True
        #if the robot is already moving and it should stop, dont change posture
        #otherwise it would try to change posture forever
        if xForwardBackward == 0.0 and yLeftRight == 0.0 and tCoordinate == 0.0:
            not_moving = False
        #set this so that the robot stands when starting moving
        if (not_moving):
            postureProxy = ALProxy("ALRobotPosture", NAO_IP_ADDRESS, NAO_PORT)
            posture = str("StandZero")
            speed = float(1.0)
            postureProxy.goToPosture(posture, speed)

        motionProxy = ALProxy("ALMotion", NAO_IP_ADDRESS, NAO_PORT)

        #set stiffness to be able to move
        StiffnessOn(motionProxy)

        motionProxy.setWalkArmsEnabled(enableArmsInWalkAlgorithm, enableArmsInWalkAlgorithm)
        motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
        motionProxy.setWalkTargetVelocity(xForwardBackward, yLeftRight, tRotation, speed)

        return jsonify({'message': 'Successfully moving', 'return_code': 200}), 200
    except ValueError as ve:
        return jsonify({'message': 'Failed to move', 'cause': str(ve), 'return_code': 400}), 400
    except Exception as e:
        return jsonify({'message': 'Failed to move', 'cause': str(e), 'return_code': 500}), 500


def StiffnessOn(proxy):
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

