from flask import Flask, render_template, jsonify
from threading import Thread
import time
import psutil

app = Flask(__name__)

# Store metrics for the dashboard
metrics = {"energy": [], "cpu": [], "memory": []}

# Background thread to monitor metrics
def monitor_metrics():
    while True:
        metrics["energy"].append(psutil.cpu_percent())
        metrics["cpu"].append(psutil.cpu_percent())
        metrics["memory"].append(psutil.virtual_memory().percent)
        if len(metrics["energy"]) > 10:
            metrics["energy"].pop(0)
            metrics["cpu"].pop(0)
            metrics["memory"].pop(0)
        time.sleep(1)

# Start monitoring thread
Thread(target=monitor_metrics, daemon=True).start()

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/metrics")
def get_metrics():
    return jsonify(metrics)

if __name__ == "__main__":
    app.run(debug=True)
