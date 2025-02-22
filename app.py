from flask import Flask, jsonify
from monitor import get_system_metrics
from alert import send_alert

app = Flask(__name__)

@app.route('/')
def home():
    return "Proactive Monitoring System Running!"

@app.route('/metrics')
def metrics():
    data = get_system_metrics()
    if data["cpu_usage"] > 80 or data["memory_usage"] > 80:
        send_alert(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
