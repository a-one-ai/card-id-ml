from roboflow import Roboflow
rf = Roboflow(api_key="Vut8iDWcQ3Ll7EMB6WiO")
project = rf.workspace("nourhan-mostafa-jaw2n").project("cropped-number")
dataset = project.version(9).download("yolov8")