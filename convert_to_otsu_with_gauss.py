import cv2
import numpy as np
from matplotlib import pyplot as plt
from image_helpers import *
from path_url_helpers import *

import os
import uuid


exts = ['.bmp']





for path, subdirs, files in os.walk('/home/naz/Desktop/symbols'):
    for name in files:
        path_and_name = os.path.join(path, name)


        fileExtension = get_extension(path_and_name)


        if fileExtension in exts:
            subdir_path = os.path.join('/home/naz/Desktop/symbols_otsu/', segment_after_last_slash(path))

            if not os.path.exists(subdir_path):
                os.makedirs(subdir_path)

            new_path_and_name = os.path.join(subdir_path, str(uuid.uuid4()) + '.png')
            # print(new_path_and_name)

            cv2.imwrite(new_path_and_name, get_image_otsu_gauss(path_and_name))







cv2.waitKey()