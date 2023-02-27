import cv2, os

#path to picture
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "img/img1.jpg")

#reading picture
img = cv2.imread(filename)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#path to Haar Cascade
filename = os.path.join(dirname, "classifier/cascade.xml")
haar_cascade = cv2.CascadeClassifier(filename)
#detection
detect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
  
for (x, y, w, h) in detect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

#detect
cv2.imshow('Detected mouse', img)
cv2.waitKey(0)