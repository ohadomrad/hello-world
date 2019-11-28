# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 08:24:31 2019

@author: Ohad Omrad YB 4
"""

import cv2
import argparse


def getImage():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help = "Path to the image")
    args = vars(ap.parse_args())
    image = cv2.imread(args["image"])
    copyimage = cv2.imread(args["image"])
    return image, copyimage

"""
def copyImage(image):
    copyimage = args(image)
    copyimage.save('copy.png')
    return copyimage
"""

def changeCornetToGreen(image):
    image[0:100, 0:100] = (0, 255, 0)
    return image
    

def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]

    if center is None:
        center = (w // 2, h // 2)

    Matrix = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, Matrix, (w, h))


def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    
    (image_h, image_w) = image.shape[:2]
    
    if width is None and height is None:
        return image
    
    elif width is None:
        width = int((height/image_h) * image_w)
        height = int((height/image_h) * image_h)
    
    elif height is None:
        height = int((width/image_w) * image_h)
        width = int((width/image_w) * image_w)
    
    
    return cv2.resize(image, (width, height), inter) 


def main():
    image, copyimage = getImage()
    cv2.imshow("Orginal", image)
   
    cv2.imshow("Updated", changeCornetToGreen(image))

    cv2.imshow("Rotated by 45 Degrees", rotate(copyimage, 45))
    rotate(copyimage, -45)
    
   
    cv2.imshow("Resized ", resize(copyimage,500))
    
    cv2.waitKey(0)


main()