from ocr import process_ocr_front, process_ocr_back ,process_two_sides
from flask import Flask, render_template, request, url_for
import os
import cv2

app = Flask(__name__)

# Define the folder where uploaded images will be stored
UPLOAD_FOLDER_PATH = "./uploaded_images"

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER_PATH):
    os.makedirs(UPLOAD_FOLDER_PATH)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/uploadfront", methods=["POST"])
def upload_image():
    if "image" in request.files:
        image = request.files["image"]
        if image.filename != "":
            img_path = os.path.join(UPLOAD_FOLDER_PATH, 'front_id',image.filename)
            image.save(img_path)
            print(f"  image.filename {image.filename}")
            print(f" *-front imag path {img_path}")
            print("type of front img ",type(image))
            osrResult = process_ocr_front(cv2.imread(img_path))
            print(osrResult)
            return {"data":osrResult}
        
@app.route("/uploadboth", methods=["POST"])
def upload_image_both():
    images = request.files.getlist("images")
    if len(images)==2:
        img_path1 = os.path.join(UPLOAD_FOLDER_PATH, 'front_id',images[0].filename)
        print("type of images[0] img ",type(images[0]))
        images[0].save(img_path1)
        img_path2 = os.path.join(UPLOAD_FOLDER_PATH, 'back_id',images[1].filename)
        images[1].save(img_path2)
        output = process_two_sides(cv2.imread(img_path2),cv2.imread(img_path1))
        return output
    else:
        return {"data":"Only one image is uploaded !"}
    
@app.route("/uploadback", methods=["POST"])
def upload_image_back():
    if "image" in request.files:
        image = request.files["image"]
        if image.filename != "":
           img_path = os.path.join(UPLOAD_FOLDER_PATH, 'back_id',image.filename)
           print(f" *-back imag path {img_path}")
           image.save(img_path)
           ocrResult = process_ocr_back(cv2.imread(img_path))
           print(ocrResult)
    return {"data":ocrResult}

if __name__ == "__main__":
    app.run(port=5000, debug=True)
    print(f"Server is running at port 5000")
