import cv2
import caffe_helpers
from lbp_helpers import *
import glob
import time
from list_helpers import *
from multiprocessing import Pool
import multiprocessing
import time

path_to_save = '/home/naz/tmp/Organizations_1993'


# Foreign_citizens_2012
# High_authorities_1993
# organizations_2012



files = glob.glob('/media/naz/3534-E743/avto_nomera_downloads/kz/Organizations_1993/*.jpg')




# for file in files:
#     print(file)
#
#     img = cv2.imread(file, cv2.IMREAD_COLOR)
#
#     # img = cv2.pyrDown(img)
#     if img is not None:
#         rects = get_lbp_rects(img)
#         save_rois_by_rects(img, rects, path_to_save)



def worker(file):
    name = multiprocessing.current_process().name

    print(file)

    img = cv2.imread(file, cv2.IMREAD_COLOR)
    # img = cv2.pyrDown(img)

    if img is not None:
        rects = get_lbp_rects(img)
        save_rois_by_rects(img, rects, path_to_save)









start = time.time()


pool_size = 4
pool = multiprocessing.Pool(processes = pool_size)
pool.map(worker, files)
pool.close()
pool.join()


print("get_lbp_rects %.2f s." % (time.time() - start))