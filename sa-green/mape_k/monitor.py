import psutil
import pyRAPL
import time

class Monitor:
    def __init__(self):
        pyRAPL.setup()
        self.energy_meter = pyRAPL.Measurement('energy_usage_monitor')
    
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
        else:
            print("Energy monitoring not available for pyRAPL. Returning None.")
            return None

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

    def get_metrics(self, confidence_scores, detections, system_type="intel"):
        energy_usage = None

        if self.use_pyrapl:
            # Ensure energy monitoring has started
            if not hasattr(self.energy_meter, '_energy_begin') or self.energy_meter._energy_begin is None:
                print("Energy monitoring was not started. Starting it now...")
                self.start_energy_monitor()  # Automatically start monitoring

            # Stop energy monitoring and fetch metrics
            energy_usage = self.stop_energy_monitor()
        elif system_type == "amd":
            energy_usage = self.get_amd_energy_usage()
        elif system_type == "mac":
            energy_usage = self.get_mac_energy_usage()
        else:
            print("Energy monitoring not supported for this system.")

        return {
            "energy_usage": energy_usage,
            "cpu_usage": self.get_cpu_usage(),
            "memory_usage": self.get_memory_usage(),
            "confidence_scores": confidence_scores,
            "detections": len(detections)
        }
