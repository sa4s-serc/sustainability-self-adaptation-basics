import psutil
import time
import subprocess
import platform
import pyRAPL

class Monitor:
    def __init__(self, cpu_tdp=105):
        self.system_type = platform.system().lower()  # Automatically detect system type
        self.use_pyrapl = False
        self.cpu_tdp = cpu_tdp

        if self.system_type == "linux":
            try:
                import pyRAPL
                pyRAPL.setup()
                self.energy_meter = pyRAPL.Measurement('energy_usage_monitor')
                self.use_pyrapl = True
            except ImportError:
                print("pyRAPL not available on Linux. Falling back to generic monitoring.")
                self.energy_meter = None
        else:
            self.energy_meter = None

    def start_energy_monitor(self):
        if self.use_pyrapl:
            self.energy_meter.begin()

    def stop_energy_monitor(self):
        if self.use_pyrapl:
            # Ensure energy monitoring was started
            if not hasattr(self.energy_meter, '_energy_begin') or self.energy_meter._energy_begin is None:
                raise RuntimeError("Energy monitoring was not started before stopping.")
            self.energy_meter.end()
            return self.energy_meter.result.pkg[0] if isinstance(self.energy_meter.result.pkg, list) else self.energy_meter.result.pkg
        elif self.system_type == "linux":
            return self.get_amd_energy_usage()
        elif self.system_type == "darwin":  # macOS
            return self.get_mac_energy_usage()
        elif self.system_type == "windows":
            print("Starting Energy monitoring for this system.")
            return self.simulate_energy_usage()
        else:
            print("Energy monitoring not available for this system.")
            return 0
        
    def simulate_energy_usage(self, duration=5):
        # Simulate energy usage based on CPU utilization and TDP
        total_energy = 0
        for _ in range(duration):
            cpu_usage = psutil.cpu_percent(interval=1) / 100  # CPU usage as a fraction
            total_energy += cpu_usage * self.cpu_tdp  # Multiply by TDP
        return total_energy  # Approximate energy in Joules

    def get_amd_energy_usage(self):
        try:
            result = subprocess.run(["likwid-perfctr", "-C", "0", "-g", "ENERGY"], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            print(f"Error using LIKWID: {e}")
            return "Energy usage not available."

    def get_mac_energy_usage(self):
        try:
            result = subprocess.run(["sudo", "powermetrics", "--samplers", "power"], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            print(f"Error using powermetrics: {e}")
            return "Energy usage not available."

    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=0.1)

    def get_memory_usage(self):
        return psutil.virtual_memory().percent

    def get_metrics(self, confidence_scores, detections):
        energy_usage = self.stop_energy_monitor()

        return {
            "energy_usage": energy_usage,
            "cpu_usage": self.get_cpu_usage(),
            "memory_usage": self.get_memory_usage(),
            "confidence_scores": confidence_scores,
            "detections": len(detections)
        }

# Example Usage
if __name__ == "__main__":
    monitor = Monitor()
    monitor.start_energy_monitor()
    time.sleep(1)  # Simulate workload
    metrics = monitor.get_metrics([0.95, 0.87], ["object1", "object2"])
    print(metrics)
