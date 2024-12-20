import time
import psutil
import numpy as np
import subprocess
from sklearn.linear_model import LinearRegression


# Function to check if pyRAPL can be used (Intel processors only)
def is_pyrapl_supported():
    try:
        import pyRAPL
        pyRAPL.setup()
        return pyRAPL.Measurement('test')
    except Exception as e:
        print(f"pyRAPL not supported: {e}")
        return None


# Function to simulate a basic model
def run_model():
    print("Running the model...")
    X = np.random.rand(1000, 10)  # Small dataset
    y = np.random.rand(1000)
    model = LinearRegression()
    model.fit(X, y)
    time.sleep(2)  # Simulate model execution time
    print("Model run complete.")


# Energy monitoring for AMD (using LIKWID)
def get_amd_energy_usage():
    try:
        result = subprocess.run(["likwid-perfctr", "-C", "0", "-g", "ENERGY"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error using LIKWID: {e}")
        return "Energy usage not available."


# Energy monitoring for Mac (using powermetrics)
def get_mac_energy_usage():
    try:
        result = subprocess.run(["sudo", "powermetrics", "--samplers", "power"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error using powermetrics: {e}")
        return "Energy usage not available."


# Function to monitor system metrics for generic systems
def monitor_metrics_generic(duration=5, system_type="generic"):
    cpu_usage = []
    memory_usage = []
    energy_usage = []

    for _ in range(duration):
        cpu_usage.append(psutil.cpu_percent(interval=1))
        memory_usage.append(psutil.virtual_memory().percent)
        if system_type == "amd":
            energy_usage.append(get_amd_energy_usage())
        elif system_type == "mac":
            energy_usage.append(get_mac_energy_usage())
        else:
            energy_usage.append("Energy monitoring not supported.")
        time.sleep(1)

    return {
        "energy_usage": energy_usage,
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage
    }


if __name__ == "__main__":
    # Check for pyRAPL support
    pyrapl_meter = is_pyrapl_supported()
    if pyrapl_meter:
        print("Using pyRAPL for energy monitoring...")
        pyrapl_meter.begin()
        metrics = monitor_metrics_generic(duration=5, system_type="intel")
        pyrapl_meter.end()
        metrics["energy_usage"] = pyrapl_meter.result.pkg[0]
    elif psutil.MACOS:
        print("Using powermetrics for energy monitoring (Mac)...")
        metrics = monitor_metrics_generic(duration=5, system_type="mac")
    elif psutil.LINUX:
        print("Using LIKWID for energy monitoring (AMD)...")
        metrics = monitor_metrics_generic(duration=5, system_type="amd")
    else:
        print("Energy monitoring not supported for this system.")
        metrics = monitor_metrics_generic(duration=5)

    run_model()
    print(metrics)
