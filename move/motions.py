robot = "test";
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
