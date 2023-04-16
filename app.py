from flask import Flask
from controller.routes import robot_controller
from robot_controller.config import NAO_IP_ADDRESS, NAO_PORT

# Create a new Flask app
app = Flask(__name__)

# Register the robot_controller Blueprint
app.register_blueprint(robot_controller)

# Set the configuration variables for the NAO robot
app.config['NAO_IP_ADDRESS'] = NAO_IP_ADDRESS
app.config['NAO_PORT'] = NAO_PORT

app.run(debug=True, port=8080)

