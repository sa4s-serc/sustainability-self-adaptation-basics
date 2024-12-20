class Plan:
    def plan_action(self, analysis_result):
        if analysis_result == "switch_model":
            return "model_b"  # Switch to Model B
        return "model_a"  # Stay on Model A
