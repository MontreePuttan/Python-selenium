import cv2
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np


webcam = cv2.VideoCapture(0)
success, image_bgr = webcam.read()

face_cascade = "haarcascade_frontalface_default.xml"

face_classifier = cv2.CascadeClassifier(face_cascade)

# เปลี่ยนการแสดงผลเป็นทศนิยม 
np.set_printoptions(suppress=True)
model = load_model("keras_Model.h5", compile=False)
size = (224, 224)

while True:
    success, image_bgr = webcam.read()

    image_org = image_bgr.copy()

    image_bw = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    
    faces = face_classifier.detectMultiScale(image_bw)

    # print(f'There are {len(faces)} faces found.')

    for face in faces:
        x, y, w, h = face
        cface_rgb = Image.fromarray(image_rgb[y:y+h,x:x+w])

        # สร้างข้อมูลที่ใช้รับขนาดที่ Model ใช้
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # สร้างข้อมูลที่ใช้รับขนาดที่ Model ใช้
        image = cface_rgb

        # ปรับขนาดข้อมูลในเป็นขนาดที่ต้องการ
        
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        # เปลี่ยนข้อมูลให้เป็น array
        image_array = np.asarray(image)

        # แสดงผลรูป
        # image.show()

        # ปรับขนาดข้อมูลสำหรับ Model
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        # นำข้อมูลใส่ data ในขนาดที่กำหนดไว้
        data[0] = normalized_image_array

        # นำข้อมูลมาวิเคราะห์ด้วย model
        prediction = model.predict(data)
        print(prediction)

        if prediction[0][0] > prediction[0][1]:
            cv2.putText(image_bgr, 'Masked', (x,y-7), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0,255,0), 2)
            cv2.rectangle(image_bgr, (x, y), (x+w, y+h), (0,255,0),2)
        else:
            cv2.putText(image_bgr, 'Non-Masked', (x,y-7), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0,0,255), 2)
            cv2.rectangle(image_bgr, (x, y), (x+w, y+h), (0,0,255),2)

    
    cv2.imshow("Mask Detection", image_bgr)
    #cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
        
webcam.release()
cv2.destroyAllWindows()
