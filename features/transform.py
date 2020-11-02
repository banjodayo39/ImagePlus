from PIL import Image
import cv2
import scipy.ndimage
import numpy as np

def v_concat(img):
    img_v = cv2.vconcat([img, img])
    return img_v

def h_concat(img):
    img_v = cv2.hconcat([img, img])
    return img_v

def rotate_clockwise(img):
    rot_image = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
    return rot_image

def rotate_counter_clockwise(img):
    rot_image = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    return rot_image

def h_concat_mirror(img):
    mirror_img = cv2.flip(img, 1)
    img_h = cv2.hconcat([img, mirror_img])
    return img_h
    
def v_concat_mirror(img):
    mirror_img = cv2.flip(img, 0)
    img_h = cv2.vconcat([img, mirror_img])
    return img_h

def overlay_bottom(img, scale= 0.25):
    print(img.shape)
    large_img = img
    height, width = img.shape[0],img.shape[1]
    w, h = int(width * scale), int(height * scale)
    small_img = cv2.resize(img, (w, h))
    h_diff = height - h
    w_diff = width - w
    large_img[ h_diff : height, w_diff : width] = small_img
    return large_img    


def overlay_center(img, scale= 0.25):
    print(img.shape)
    large_img = img
    height, width = img.shape[0],img.shape[1]
    w, h = int(width * scale), int(height * scale)
    small_img = cv2.resize(img, (w, h))
    h_top = int(height * 0.375)
    w_top = int(width * 0.375)
    large_img[ h_top : h_top + h, w_top : w_top + w] = small_img
    return large_img     

def stitch_image(images):
    no_of_images = len(images)

    for i in range(no_of_images):
        images[i] = imutils.resize(images[i], width=400)

    for i in range(no_of_images):
        images[i] = imutils.resize(images[i], height=400)
    stitcher = cv2.Stitcher.create()
    (status,result) = stitcher.stitch(images)
    if (status == cv2.STITCHER_OK):
        print('Panorama Generated')
    return result 

