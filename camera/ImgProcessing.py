# -*- coding: utf-8 -*-
"""
@author:qct
this code is for image processiong like photoshop
"""
import cv2
import os 

class ImgProcessor:
    def __init__(self):
        print("it is a new ImgProcessor object")

    def showImg(self,img_path):
        img_path
        img = cv2.imread(img_path)
        cv2.imshow("img",img)


#test for ustc photo
import sys

imgs_dir = "C:\\Users\\Administrator\\Desktop\\ustc_photo"
imgs_path = os.listdir(imgs_dir)
sys.path.append(imgs_dir)
ip = ImgProcessor()
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
for img_path in imgs_path:
    ip.showImg(os.path.join(imgs_dir,img_path))   
    cv2.waitKey(3000)

