import time
import psutil
import numpy as np
import pyRAPL
from sklearn.linear_model import LinearRegression

pyRAPL.setup()

# Function to simulate a basic model
def run_model():
    print("Running the model...")
    X = np.random.rand(1000, 10)  # Small dataset
    y = np.random.rand(1000)
    model = LinearRegression()
    model.fit(X, y)
    time.sleep(2)  # Simulate model execution time
    print("Model run complete.")

# Function to monitor system metrics
def monitor_metrics(duration=5):
    energy_usage = []
    cpu_usage = []
    memory_usage = []

    psutil.cpu_percent(interval=None)

    for _ in range(duration):
        # Simulating energy usage (via CPU utilization)
        #energy_usage.append(psutil.cpu_percent())
        energy_usage.append(pyRAPL.measurement.Measurement('energy').result.pkg)
        cpu_usage.append(psutil.cpu_percent(interval=1))
        memory_usage.append(psutil.virtual_memory().percent)
        time.sleep(1)

    return {
        "energy_usage": energy_usage,
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage
    }

if __name__ == "__main__":
    metrics = monitor_metrics()
    run_model()
    print(metrics)
