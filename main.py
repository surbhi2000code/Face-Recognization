import cv2
def face_detect(img_dir):
    img = cv2.imread(img_dir)
    gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    FaceRecog = cv2.CascadeClassifier('face_recog_data.xml')
    cor = FaceRecog.detectMultiScale(gimg, 1.3, 5)
    try:
        if cor.all():
            for (x, y, w, h) in cor:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
            return img
    except AttributeError:
        return img
cv2.imshow('X', face_detect('peoples.jpg'))
cv2.waitKey()