import cv2
import numpy as np
import tensorflow as tf

# Load MobileNet TFLite model
interpreter = tf.lite.Interpreter(model_path="models/1.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def preprocess_image(image):
    """Preprocess the input image for MobileNet."""
    input_shape = input_details[0]['shape']
    resized = cv2.resize(image, (input_shape[1], input_shape[2]))
    normalized = resized / 255.0
    # Check input type and preprocess accordingly
    if input_details[0]['dtype'] == np.uint8:
        # Quantized model (UINT8)
        preprocessed = resized.astype('uint8')
    else:
        # Float model (FLOAT32)
        preprocessed = resized.astype('float32') / 255.0

    return np.expand_dims(preprocessed, axis=0)
    #return np.expand_dims(normalized.astype(np.float32), axis=0)

def postprocess_output(output_data, image_shape):
    """Post-process the output data from MobileNet."""
    detections = []
    for detection in output_data:
        # Ensure detection has expected length
        if len(detection) >= 2:
            confidence = detection[1]
            if confidence > 0.5:  # Filter based on confidence threshold
                bbox = detection[2:6]  # Extract bounding box (example format)
                detections.append({"confidence": confidence, "bbox": bbox})

    return detections
#        confidence = detection[1]
#        if confidence > 0.5:  # Confidence threshold
#            bbox = detection[2:6] * [image_shape[1], image_shape[0], image_shape[1], image_shape[0]]
#            x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2] - bbox[0]), int(bbox[3] - bbox[1])
#            detections.append({"x": x, "y": y, "w": w, "h": h, "confidence": confidence})
#    return detections

def infer(image):
    """Perform inference using MobileNet."""
    input_data = preprocess_image(image)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    detections = postprocess_output(output_data, image.shape)
#    confidence_scores = [det['confidence'] for det in detections]
    return {"confidence_scores": detections, "detections": detections}
