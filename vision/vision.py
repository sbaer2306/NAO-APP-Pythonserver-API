import cv2
import numpy as np
from flask import jsonify, Response
from robot_controller.config import NAO_PORT,NAO_IP_ADDRESS
from naoqi import ALProxy
import qi

def get_brightness():
    try:
        videoProxy = ALProxy("ALVideoDevice", NAO_IP_ADDRESS,NAO_PORT)
        # top camera (0) brightness parameter (0)
        brightness=videoProxy.getParameter(0,0)
        return jsonify({ 'brightness': brightness, 'return_code': 200}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to get brightness','cause': str(e), 'return_code': 500}), 500


def set_brightness(request):
    try:
        brightness = request.json.get('brightness')
        if brightness is None:
            raise ValueError("Brightness parameter is not set")
        brightness = int(brightness)
        if ((brightness <= 255) and (brightness >= 0)):
            brightness = int(brightness)
            videoProxy = ALProxy("ALVideoDevice", NAO_IP_ADDRESS, NAO_PORT)
            #top camera (0) brightness parameter (0)
            videoProxy.setParameter(0, 0, brightness)
            return jsonify({'message': 'Successfully set brightness', 'return_code': 200}), 200
        else:
            raise ValueError("Brightness parameter out of range (0-255)")
    except ValueError as ve:
        return jsonify({'message': 'Failed to set brightness', 'cause': str(ve), 'return_code': 400}), 400
    except Exception as e:
        return jsonify({'message': 'Failed to set brightness', 'cause': str(e), 'return_code': 500}), 500

def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def generate_frames():
    # Verbindung zum NAO-Roboter herstellen
    session = qi.Session()
    session.connect("tcp://" + "127.0.0.1" + ":" + str(NAO_PORT))
    camera = session.service("ALVideoDevice")

    # Kameraparameter festlegen
    camera_name = "camera"
    camera_resolution = 2
    camera_color_space = 13
    camera_fps = 15

    camera_handle = camera.subscribeCamera(
        camera_name, 0, camera_resolution, camera_color_space, camera_fps
    )

    while True:
        # Bild von der Kamera abrufen
        image = camera.getImageRemote(camera_handle)

        # Bild in OpenCV-Format konvertieren
        width, height = image[0], image[1]
        array = image[6]
        frame = np.frombuffer(array, dtype=np.uint8).reshape((height, width, 3))

        # Bild als JPEG kodieren
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Kamera-Stream beenden
    camera.unsubscribe(camera_handle)



