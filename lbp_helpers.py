import cv2
from common import clock, draw_str
import os
import uuid

def detect(img):
    cascade = cv2.CascadeClassifier('/home/naz/Desktop/CropNumbers_LBP/haarcascade/cascade.xml')

    rects = cascade.detectMultiScale(img, scaleFactor=1.01, minNeighbors=1, minSize=(20, 20), flags = cv2.CASCADE_SCALE_IMAGE)

    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]

    return rects



def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)



# get proposed rectangles from LBP cascade
def get_lbp_rects(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    t = clock()
    rects = detect(gray)
    dt = clock() - t



    return rects




# img - original image form which to extract ROIs
# rects - coordinates of the ROIs
def save_rois_by_rects(img, rects, path):
    for rect in rects:
        x1, y1, x2, y2 = rect
        roi = img[y1:y2, x1:x2]
        # cv2.imshow('roi' + str(x1) + str(x2), roi)
        cv2.imwrite(os.path.join(path, str(uuid.uuid4()) + '.png'), roi)