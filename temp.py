#!/usr/local/bin python2.7

import numpy as np 
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("./datasets/Colosseum.png", 0)

if img is not None:

	cv2.imshow('YES!', img)

	cv2.waitKey(0)

	cv2.destroyAllWindows()
	
	plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

	plt.xticks([]), plt.yticks([])

	plt.show