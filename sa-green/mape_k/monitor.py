import pyRAPL
import psutil
import time
import subprocess

class Monitor:
    def __init__(self, system_type="intel"):
        self.system_type = system_type
        self.use_pyrapl = False

        if system_type == "intel":
            try:
                import pyRAPL
                pyRAPL.setup()
                self.energy_meter = pyRAPL.Measurement('energy_usage_monitor')
                self.use_pyrapl = True
            except ImportError:
                print("pyRAPL not available. Falling back to generic monitoring.")
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
        elif self.system_type == "amd":
            return self.get_amd_energy_usage()
        elif self.system_type == "mac":
            return self.get_mac_energy_usage()
        else:
            print("Energy monitoring not available for this system.")
            return "Not available"

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
