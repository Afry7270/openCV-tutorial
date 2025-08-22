import cv2

################################################################
path = 'assets/MosquitoCascade.xml'  # PATH OF THE CASCADE
cameraNo = 0                    # CAMERA NUMBER
objectName = 'Mosquito'       # OBJECT NAME TO DISPLAY
frameWidth= 1080                     # DISPLAY WIDTH
frameHeight = 720                  # DISPLAY HEIGHT
color= (255,0,255)
#################################################################


cap = cv2.VideoCapture(cameraNo)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

# CREATE TRACKBAR
cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",180,1000,empty)
cv2.createTrackbar("Neig","Result",8,50,empty)
cv2.createTrackbar("Min Area","Result",0,100000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)

# LOAD THE CLASSIFIERS DOWNLOADED
cascade = cv2.CascadeClassifier(path)

while True:
    # SET CAMERA BRIGHTNESS FROM TRACKBAR VALUE
    cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    cap.set(10, cameraBrightness)
    # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # DETECT THE OBJECT USING THE CASCADE
    scaleVal =1 + (cv2.getTrackbarPos("Scale", "Result") /1000)
    neig=cv2.getTrackbarPos("Neig", "Result")
    objects = cascade.detectMultiScale(gray,scaleVal, neig)


    # DISPLAY THE DETECTED OBJECTS
    for (x,y,w,h) in objects:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        if area >minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            roi_color = img[y:y+h, x:x+w]
   
    count = str(len(objects))
    cv2.putText(img, f'count: {count}',(10,25),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)



    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
cap.release()
cv2.destroyAllWindows()