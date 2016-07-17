import numpy as np
import cv2
#import argparse


#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image")
#args = vars(ap.parse_args())

image = cv2.imread("./datasets/Colosseum.png")

width = image.shape[1]
height = image.shape[0]

#image[::] = (100,100,100)

final = np.zeros((height,width, 3), np.uint8)

for x in xrange(height-1):
	for y in xrange(width-1):
		# copying blue pixel
		final.itemset((x, y, 0), image.item(x, y, 0))
		# copying green pixel
		final.itemset((x, y, 1), image.item(x, y, 1))
		# copying red pixel
		final.itemset((x, y, 2), image.item(x, y, 2))

# writing output image
cv2.imwrite("./results/result.bmp", final)
