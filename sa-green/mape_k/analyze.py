class Analyze:
    def analyze_metrics(self, metrics):
        # Thresholds for switching models
        if metrics['energy_usage'] > 4:  # Energy usage in Joules
            return "switch_model"
        return "keep_model"
