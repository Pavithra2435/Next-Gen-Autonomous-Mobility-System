from flask import Flask, render_template, request
from motor_control import move_forward, move_backward, turn_left, turn_right, stop, set_speed
from sensors import get_lane_status, get_distance
import threading
import time

app = Flask(__name__)

mode = "manual"  # default mode


# ---------- Autonomous Modes ----------

def object_avoidance_mode():
    global mode
    while mode == "object":
        dist = get_distance()

        if dist < 20:
            stop()
            time.sleep(0.3)
            turn_left()
            time.sleep(0.5)
            stop()
        else:
            move_forward()

        time.sleep(0.1)


def lane_follow_mode():
    global mode
    while mode == "lane":
        left, right = get_lane_status()

        if left == 0 and right == 0:
            move_forward()
        elif left == 0 and right == 1:
            turn_left()
        elif left == 1 and right == 0:
            turn_right()
        else:
            stop()

        time.sleep(0.1)


# ---------- Routes ----------

@app.route('/')
def index():
    return render_template('control.html', mode=mode)


@app.route('/move', methods=['POST'])
def move():
    global mode
    action = request.form['action']

    if action == "forward":
        move_forward()
    elif action == "backward":
        move_backward()
    elif action == "left":
        turn_left()
    elif action == "right":
        turn_right()
    elif action == "stop":
        stop()

    elif action == "manual":
        mode = "manual"
        stop()

    elif action == "object":
        mode = "object"
        threading.Thread(target=object_avoidance_mode, daemon=True).start()

    elif action == "lane":
        mode = "lane"
        threading.Thread(target=lane_follow_mode, daemon=True).start()

    return ("", 204)


@app.route('/set_speed/<int:value>')
def set_speed_route(value):
    set_speed(value)
    return ("", 204)


# ---------- Main ----------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)