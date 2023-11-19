from ultralytics import YOLO
from onnx import TensorProto
from onnx.helper import (
    make_model, make_node, make_graph,
    make_tensor_value_info)
from onnx.checker import check_model

model = "/home/paperspace/train-offline/card-id-ml/runs/detect/train7/weights/best.pt"


# Export the model to ONNX format
success = model.export(format='onnx')
