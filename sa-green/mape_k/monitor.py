import psutil
import pyRAPL
import time

class Monitor:
    def __init__(self):
        pyRAPL.setup()
        self.energy_meter = pyRAPL.Measurement('energy_usage_monitor')
    
    def start_energy_monitor(self):
        self.energy_meter.begin()
    
    def stop_energy_monitor(self):
        # Ensure energy monitoring was started
        if not hasattr(self.energy_meter, '_energy_begin') or self.energy_meter._energy_begin is None:
            raise RuntimeError("Energy monitoring was not started before stopping.")
        self.energy_meter.end()
        return self.energy_meter.result.pkg[0] #if isinstance(self.energy_meter.result.pkg, list) else result.pkg
    
    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=0.1)
    
    def get_memory_usage(self):
        return psutil.virtual_memory().percent

    def get_metrics(self, confidence_scores, detections):
        # Ensure energy monitoring has started
        if not hasattr(self.energy_meter, '_energy_begin') or self.energy_meter._energy_begin is None:
            print("Energy monitoring was not started. Starting it now...")
            self.start_energy_monitor()  # Automatically start monitoring
    
        # Stop energy monitoring and fetch metrics
        energy_usage = self.stop_energy_monitor()
        return {
            "energy_usage": energy_usage,
            "cpu_usage": self.get_cpu_usage(),
            "memory_usage": self.get_memory_usage(),
            "confidence_scores": confidence_scores,
            "detections": len(detections)
        }
