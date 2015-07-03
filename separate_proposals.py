import glob
import os
from caffe_helpers import *
# import cv2
import Image
from shutil import *
import uuid

path = '/media/naz/3534-E743/avto_nomera_downloads/kz_crops/High_authorities_1993/'





plates_path = '/home/naz/Desktop/classified_plates_2'

files = glob.glob(os.path.join(path, '*.png'))



classifier = init_caffe_netwrok()





for k in range(0, len(files), 1000):



    print(k)

    predictions = classify_many(files[k:k+1000], classifier)



    print(predictions)

    for i, pred in enumerate(predictions):

        if np.argmax(pred) == 1:
            # print('moving')
            move(files[k:k+1000][i], os.path.join(plates_path, str(uuid.uuid4())))







