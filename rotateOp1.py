import numpy as np
import cv2

def rotate180(path, name):

	image = cv2.imread(path)

	height = image.shape[0]
	width = image.shape[1]

	final = np.zeros((height, width, 3), np.uint8)

	b = image[:, :, 0]
	g = image[:, :, 1]
	r = image[:, :, 2]

	
	print b
	print "==============="
	print g
	print "==============="
	print r
	print "==============="
	print len(b), len(g), len(r)
	print "==============="
	print len(b[0]), len(g[0]), len(r[0]), "\n"


rotate180("./datasets/Colosseum.png", None)