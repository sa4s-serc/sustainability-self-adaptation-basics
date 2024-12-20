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
        self.energy_meter.end()
        return sum(self.energy_meter.result.pkg) if isinstance(self.energy_meter.result.pkg, list) else result.pkg
    
    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=0.1)
    
    def get_memory_usage(self):
        return psutil.virtual_memory().percent

    def get_metrics(self, confidence_scores, detections):
        return {
            "energy_usage": self.stop_energy_monitor(),
            "cpu_usage": self.get_cpu_usage(),
            "memory_usage": self.get_memory_usage(),
            "confidence_scores": confidence_scores,
            "detections": len(detections)
        }
