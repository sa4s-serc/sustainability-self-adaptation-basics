from flask import Flask, render_template
from mape_k.monitor import Monitor
import time
import os

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Pass metrics to the template
    monitor = Monitor()
    monitor.start_energy_monitor()  # Start energy monitoring
    time.sleep(1)  # Simulate workload or replace with actual work
    metrics = monitor.get_metrics([], [])
    return render_template('dashboard.html', metrics=metrics)

if __name__ == "__main__":
    app.run(debug=True)
