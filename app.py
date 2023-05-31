from flask import Flask, request, abort
from controller.routes import robot_controller
from robot_controller.config import NAO_IP_ADDRESS,NAO_PORT

# Create a new Flask app
app = Flask(__name__)

# Register the robot_controller Blueprint
app.register_blueprint(robot_controller)

# Set the configuration variables for the NAO robot
app.config['NAO_IP_ADDRESS'] = NAO_IP_ADDRESS
app.config['NAO_PORT'] = NAO_PORT

@app.before_request
def before_request():
    if request.path.startswith('/api'):
        if 'application/json' not in request.headers.get('Content-Type'):
            abort(400, 'Request Content-Type must be application/json')

app.run(debug=True, host='0.0.0.0', port=8080)

