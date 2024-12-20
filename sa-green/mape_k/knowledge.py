class Knowledge:
    def __init__(self):
        self.history = []

    def update_knowledge(self, metrics):
        self.history.append(metrics)
