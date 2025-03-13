import cv2

face_image = cv2.imread('rajeev rishika aarush.jpg')
grey_img = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_detect = face_cascade.detectMultiScale(face_image, scaleFactor=1.1, minNeighbors=5)
print("faces found: {}".format(len(face_detect)))
print(face_detect)
for (x, y, w, h) in face_detect:
    cv2.rectangle(face_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Image', face_image)
cv2.waitKey(0)
cv2.destroyAllWindows()