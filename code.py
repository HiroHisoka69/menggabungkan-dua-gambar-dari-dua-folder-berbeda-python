# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 13:34:56 2022

@author: hirohisoka
"""

import cv2
import glob
import os.path
import numpy as np

path1 = "folder1/*.jpg"
path2 = "folder2/*.tif"

for file1,file2 in zip(glob.glob(path1), glob.glob(path2)):
    # e.g. MyPhoto.jpg
    basename = os.path.basename(file1)
    # e.g. MyPhoto
    name = os.path.splitext(basename)[0]
    
    
    #read img
    image_folder1 = cv2.imread(file1)
    image_folder2 = cv2.imread(file2)
    
    combine = cv2.add(image_folder1,image_folder2)
    cv2.imwrite('result/' + name + '.jpg', combine)#save
