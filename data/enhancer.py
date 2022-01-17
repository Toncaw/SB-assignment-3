import glob
import os
import shutil
import numpy as np
import cv2
from scipy import ndimage

# source_folder = r"mypredictions\test\\"
#
source_folder = r"mypredictions\train\\"
#
# source_folder = r"perfectly_detected_ears\train\\"

# source_folder = r"perfectly_detected_ears\test\\"


# # SHARPEN
# for folder in os.listdir(source_folder):
#     for file_name in os.listdir(source_folder+str(folder)):
#         img = cv2.imread(source_folder+folder+'\\'+file_name)
#         kernel = np.array([[0, -1, 0],
#                            [-1, 5, -1],
#                            [0, -1, 0]])
#         image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
#         cv2.imwrite(source_folder+folder+'\\sharpen_'+file_name, image_sharp)
#         break
#
# # BLUR
# for folder in os.listdir(source_folder):
#     for file_name in os.listdir(source_folder+str(folder)):
#         if(len(file_name) < 9):
#             img = cv2.imread(source_folder+folder+'\\'+file_name)
#             blur = cv2.blur(img, (5, 5))
#             cv2.imwrite(source_folder+folder+'\\blur_'+file_name, blur)
#             break


def sharpImg(img):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

    return image_sharp

def blurImg(img):
    blur = cv2.blur(img, (5, 5))
    return blur

def flattenImg(img):
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    return img_output

for folder in os.listdir(source_folder):
    for file_name in os.listdir(source_folder+str(folder)):
        # cv2.imshow("image", retunFlattenImg(source_folder+folder+'\\'+file_name))
        # cv2.imshow("image", cv2.imread(source_folder+folder+'\\'+file_name, 0))
        # cv2.imshow("image", cv2.imread(source_folder+folder+'\\'+file_name, 0))
        # cv2.imshow("image", ndimage.rotate(cv2.imread(source_folder+folder+'\\'+file_name, 0)))
        # key = cv2.waitKey(0)
        for i in range(0, -35, -5):
            slika = ndimage.rotate(cv2.imread(source_folder+folder+'\\'+file_name),i)
            cv2.imwrite(source_folder+folder+'\\flat_'+str(i)+'_'+file_name, flattenImg(slika))
            cv2.imwrite(source_folder+folder+'\\blur_'+str(i)+'_'+file_name, blurImg(slika))
            cv2.imwrite(source_folder+folder+'\\sharp_'+str(i)+'_'+file_name, sharpImg(slika))

        for i in range(5, 35, 5):
            slika = ndimage.rotate(cv2.imread(source_folder+folder+'\\'+file_name),i)
            cv2.imwrite(source_folder+folder+'\\flat_'+str(i)+'_'+file_name, flattenImg(slika))
            cv2.imwrite(source_folder+folder+'\\blur_'+str(i)+'_'+file_name, blurImg(slika))
            cv2.imwrite(source_folder+folder+'\\sharp_'+str(i)+'_'+file_name, sharpImg(slika))

    print('Saved:', file_name)