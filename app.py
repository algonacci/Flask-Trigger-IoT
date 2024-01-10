from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initial LED state (OFF)
led_state = False


@app.route('/')
def index():
    return render_template('index.html', led_state=led_state)


@app.route('/get_led_state', methods=['GET'])
def get_led_state():
    return jsonify({'led_state': 'ON' if led_state else 'OFF'})


@app.route('/toggle_led', methods=['POST'])
def toggle_led():
    global led_state
    led_state = not led_state
    return jsonify({'success': True, 'led_state': led_state})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
