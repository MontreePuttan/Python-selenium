from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# Disable scientific notation for clarity
# เปลี่ยนการแสดงผลเป็นทศนิยม 
np.set_printoptions(suppress=True)

# Load the model
# นำโมเดลที่ Train มาใช้งาน
model = load_model("keras_Model.h5", compile=False)

# Load the labels
#class_names = open("labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
# สร้างข้อมูลที่ใช้รับขนาดที่ Model ใช้
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
# สร้างข้อมูลที่ใช้รับขนาดที่ Model ใช้
image = Image.open("mask_78.jpg").convert("RGB")

# resizing the image to be at least 224x224 and then cropping from the center
# ปรับขนาดข้อมูลในเป็นขนาดที่ต้องการ
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# turn the image into a numpy array
# เปลี่ยนข้อมูลให้เป็น array
image_array = np.asarray(image)

# display the resized image
# แสดงผลรูป
image.show()

# Normalize the image
# ปรับขนาดข้อมูลสำหรับ Model
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
# นำข้อมูลใส่ data ในขนาดที่กำหนดไว้
data[0] = normalized_image_array

# Predicts the model
# นำข้อมูลมาวิเคราะห์ด้วย model
prediction = model.predict(data)
print(prediction)

#index = np.argmax(prediction)
#class_name = class_names[index]
#confidence_score = prediction[0][index]

# Print prediction and confidence score
#print("Class:", class_name[2:], end="")
#print("Confidence Score:", confidence_score)
