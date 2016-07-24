import numpy as np 
import cv2 
'''
import argparse

ap = argparse.ArgumentParser(description = "Computing different convolutional operations on the specified images",
	epilog = "In the program folder you'll find a new folder named results. Go there and check some cool stuff!")

ap.add_argument("images", metavar = "IMAGES", type = str, help = "path to the images")

args = vars(ap.parse_args())
'''

img = cv2.imread("./datasets/C.png")

conv = np.matrix([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

if img is None:
	raise Exception('can\'t open image, path might be wrong')

# transposing convolution matrix in case it's not symmetric
#conv_sharpen = conv.getT()

conv_h, conv_w = conv.shape

h = img.shape[0]
w = img.shape[1]

min_ind = -(conv_h/2)
max_ind = (conv_w/2)+1

limit_h = h
limit_w = w

final = np.zeros((h, w, 3), np.uint8)

for x in xrange(h):
	for y in xrange(w-1):

		b = 0
		g = 0
		r = 0

		for xx in xrange(min_ind, max_ind):
			for yy in xrange(min_ind, max_ind):
				
				#print x+xx, y+yy, limit_h, limit_w
				#print "======="
				#print yy
				if x+xx >= limit_h or y+yy >= limit_w or x+xx < 0 or y+yy < 0:
					continue
				else:
					b = (b + (img.item(x+xx, y+yy, 0)*conv[xx+max_ind-1,yy+max_ind-1]))%255
					g = (g + (img.item(x+xx, y+yy, 1)*conv[xx+max_ind-1,yy+max_ind-1]))%255
					r = (r + (img.item(x+xx, y+yy, 2)*conv[xx+max_ind-1,yy+max_ind-1]))%2255

		# blu pixel 
		final.itemset((x, y, 0), b)
		# green pixel
		final.itemset((x, y, 1), g)
		# red pixel
		final.itemset((x, y, 2), r)


cv2.imwrite("./results/conv/temp.png", final)
