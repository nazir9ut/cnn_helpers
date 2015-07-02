import cv2



def get_image_otsu_gauss(path_and_name):
    img = cv2.imread(path_and_name, 0)

    blur = cv2.GaussianBlur(img,(5,5),0)

    ret3,th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return th3




def get_image_otsu_gauss_inverted(path_and_name):
    img = cv2.imread(path_and_name, 0)

    blur = cv2.GaussianBlur(img,(5,5),0)

    ret3,th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    return th3




