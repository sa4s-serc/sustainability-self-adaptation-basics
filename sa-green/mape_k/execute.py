from models import model_a, model_b

class Execute:
    def execute_inference(self, model_name, image):
        if model_name == "model_a":
            return model_a.infer(image)
        else:
            return model_b.infer(image)
