import numpy as np
import cv2
#import argparse


#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image")
#args = vars(ap.parse_args())

image = cv2.imread("./Colosseum.png")

width = image.shape[1]
height = image.shape[0]


print(width, height)
