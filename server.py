from main import read_id
from flask import Flask, render_template, request
import os
import cv2
import numpy as np
from logger_config import setup_logger
import time

app = Flask(__name__)
# Define the folder where uploaded images will be stored
UPLOAD_FOLDER_PATH = "./uploaded_images"

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER_PATH):
    os.makedirs(UPLOAD_FOLDER_PATH)

# Setup logger
request_logger = setup_logger('request_logger', 'requests.log')

@app.before_request
def before_request_func():
    request.start_time = time.time()

@app.after_request
def after_request_func(response):
    duration = time.time() - request.start_time
    request_logger.info(f"Request took {duration} seconds")
    return response


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/getCardID", methods=["POST"])
def upload_image():
    if "image" in request.files:
        image = request.files["image"]
        if image.filename != "":
            try:
                image_bytes = image.read()
                np_array = np.frombuffer(image_bytes, np.uint8)
                image_cv2 = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
                ocrResult = read_id(image_cv2)
                return {"data": ocrResult}
            except Exception as error:
                print(
                    f"Error {type(error)} occurred while processing the image: {error}"
                )
                return {"data": "Please, Re-take the ID Card !!!"}
        else:
            return {"data": "Please, Re-take the ID Card !"}
    else:
        return {"data": "Only images are allowed to be uploaded !"}


port = 5000
if __name__ == "__main__":
    app.run(port=port)
    print(f"Server is running at port {port}")
