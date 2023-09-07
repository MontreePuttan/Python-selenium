import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
        coords = []
        for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+y,y+h),color,2)
                cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
                coords=[x,y,w,h]
        return img,coords

def detect(img,faceCascade):
        img,coords = draw_boundary(img,faceCascade,1.1,10,(0,0,255),"Face")
        img,coords = draw_boundary(img,eyeCascade,1.1,10,(255,0,0),"Eye")
        return img

#cap = cv2.VideoCapture("Coin2.mp4")
cap = cv2.VideoCapture(0)
while (True):
        ret,frame = cap.read()
        frame = detect(frame,faceCascade)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()