import numpy as np
import cv2
#import argparse


#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image")
#args = vars(ap.parse_args())


def rotateLeft(path, name):
	image = cv2.imread(path)

	height = image.shape[0]
	width = image.shape[1]

	final = np.zeros((width, height, 3), np.uint8)

	for x in xrange(height):
		for y in xrange(width):
			# copying blue pixel
			final.itemset((y, x, 0), image.item(x, y, 0))
			# copying green pixel
			final.itemset((y, x, 1), image.item(x, y, 1))
			# copying red pixel
			final.itemset((y, x, 2), image.item(x, y, 2))

	# writing output image
	cv2.imwrite("./results/" + name + ".png", final)


def copy(path, name):

	image = cv2.imread(path)

	height = image.shape[0]
	width = image.shape[1]

	final = np.zeros((height, width, 3), np.uint8)

	for x in xrange(height):
		for y in xrange(width):
			# copying blue pixel
			final.itemset((x, y, 0), image.item(x, y, 0))
			# copying green pixel
			final.itemset((x, y, 1), image.item(x, y, 1))
			# copying red pixel
			final.itemset((x, y, 2), image.item(x, y, 2))

	# writing output image
	cv2.imwrite("./results/" + name + ".png", final)

def rotate180(path, name):

	image = cv2.imread(path)

	height = image.shape[0]
	width = image.shape[1]

	final = np.zeros((height, width, 3), np.uint8)

	for x in xrange(height):
		for y in xrange(width):
			# copying blue pixel
			final.itemset((height-1-x, width-1-y, 0), image.item(x, y, 0))
			# copying green pixel
			final.itemset((height-1-x, width-1-y, 1), image.item(x, y, 1))
			# copying red pixel
			final.itemset((height-1-x, width-1-y, 2), image.item(x, y, 2))

	# writing output
	cv2.imwrite("./results/" + name + ".png", final)

def rotateRight(path, name):

	image = cv2.imread(path)

	height = image.shape[0]
	width = image.shape[1]

	final = np.zeros((width, height, 3,), np.uint8)

	for x in xrange(height):
		for y in xrange(width):
			# copying blue pixel
			final.itemset((width-1-y, height-1-x, 0), image.item(x, y, 0))
			# copying green pixel
			final.itemset((width-1-y, height-1-x, 1), image.item(x, y, 1))
			# copying red pixel
			final.itemset((width-1-y, height-1-x, 2), image.item(x, y, 2))

	cv2.imwrite("./results/" + name + ".png", final)


copy("./datasets/Colosseum.png", "colCopy")

rotate180("./datasets/Colosseum.png", "col180")

rotateLeft("./datasets/Colosseum.png", "colLeft")

rotateRight("./datasets/Colosseum.png", "colRight")

