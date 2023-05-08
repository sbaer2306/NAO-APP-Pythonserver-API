import cv2
from flask import jsonify
from robot_controller.config import NAO_PORT,NAO_IP_ADDRESS
from naoqi import ALProxy

def get_brightness():
    try:
        videoProxy = ALProxy("ALVideoDeviceProxy", NAO_IP_ADDRESS,NAO_PORT)
        brightness=videoProxy.getParameter(0,'Brightness')
        return jsonify({ 'brightness': brightness, 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to get brightness', 'return_code': 500}), 500
def set_brightness(request):
    try:
        brightness = request.json.get('brightness')
        videoProxy = ALProxy("ALVideoDeviceProxy", NAO_IP_ADDRESS,NAO_PORT)
        videoProxy.setParameter(0,'Brightness',brightness)
        return jsonify({'message': 'Successfully set brightness', 'brightness': brightness, 'return_code': 200}), 200
    except:
        return jsonify({'message': 'Failed to set brightness', 'return_code': 500}), 500
def get_camera():
    def generate():
        while True:
            # Get raw image from camera feed
            raw_image = camera_proxy.getImageRemote(camera_id)

            # Process image using OpenCV
            # Example: Convert to grayscale
            processed_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)

            # Encode image as JPEG
            ret, jpeg = cv2.imencode(".jpg", processed_image)

            # Yield JPEG data as response
            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n")

    # Return response containing JPEG data
    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")

def show_camera():
    camera_proxy = ALProxy("ALVideoDevice", NAO_IP_ADDRESS, NAO_PORT)

    # Set camera parameters
    resolution = 2  # 640x480
    color_space = 11  # RGB

    # Subscribe to camera feed
    camera_id = camera_proxy.subscribe("my_camera", resolution, color_space, 5)

    # Loop to continuously process video feed
    while True:
        # Get raw image from camera feed
        raw_image = camera_proxy.getImageRemote(camera_id)

        # Process image using OpenCV
        # Example: Convert to grayscale
        processed_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)

        # Display image in window
        cv2.imshow("Camera Feed", processed_image)

        # Wait for key press to exit
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    # Cleanup
    cv2.destroyAllWindows()
    camera_proxy.unsubscribe(camera_id)


