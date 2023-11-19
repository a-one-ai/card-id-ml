from ultralytics import YOLO

# Create a new YOLO model from scratch using configuration from a YAML file
model = YOLO('yolov8s.yaml')

# Alternatively, load a pretrained YOLO model (this is generally recommended for improved performance)
model = YOLO('yolov8s.pt')

# Train the model using the 'coco128.yaml' dataset for 3 epochs with a specific image size
# Adjust 'imgsz' to the desired image size for training
results = model.train(data='/home/paperspace/train-offline/card-id-ml/cropped-number-9/data.yaml', epochs=150, imgsz=416, device='cuda:0')

# Evaluate the model's performance on your custom dataset
# Replace 'your_dataset.yaml' with the path to your dataset configuration file
results = model.val(data='/home/paperspace/train-offline/card-id-ml/cropped-number-9/data.yaml')

# Perform object detection on a local image file
# Replace 'path/to/your/image.jpg' with the actual file path to your image
results = model('/home/paperspace/train-offline/card-id-ml/cropped-number-9/test/images/101_jpg.rf.da8989ae3b8bb6cba2f31165e0c85ae2.jpg')

# Export the model to ONNX format
success = model.export(format='onnx')
