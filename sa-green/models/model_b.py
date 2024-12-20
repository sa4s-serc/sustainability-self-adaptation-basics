import cv2
import numpy as np
import tensorflow as tf

# Load EfficientDet TFLite model
interpreter = tf.lite.Interpreter(model_path="models/EfficientdetliteV0MetadataV1.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def preprocess_image(image):
    """Preprocess the input image for EfficientDet."""
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
    # Extract outputs
    detection_boxes = output_data[0]  # [N, 4]
    detection_classes = output_data[1][0]  # [N]
    detection_scores = output_data[2][0]  # [N]
    num_detections = int(output_data[3][0])  # Number of valid detections

    detections = []

    # Iterate through valid detections
    for i in range(num_detections):
        confidence = detection_scores[i]
        if confidence > 0.5:  # Confidence threshold
            bbox = detection_boxes[i]
            class_id = int(detection_classes[i])

            # Normalize bounding box coordinates (if needed)
            x_min, y_min, x_max, y_max = bbox
            x_min = max(0, x_min)
            y_min = max(0, y_min)
            x_max = min(image_shape[1], x_max)
            y_max = min(image_shape[0], y_max)

            # Append detection
            detections.append({
                "class": class_id,
                "confidence": confidence,
                "bbox": [x_min, y_min, x_max, y_max]
            })

    return detections


def infer(image):
    input_data = preprocess_image(image)
    
    # Perform inference
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    
    # Get results
    output_data = [interpreter.get_tensor(output_details[i]['index']) for i in range(len(output_details))]
    
    detections = postprocess_output(output_data, image.shape)
    
    return {
        "confidence_scores": [d["confidence"] for d in detections],
        "detections": detections
    }
