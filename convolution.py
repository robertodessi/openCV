import numpy as np 
import cv2 

'''
import argparse

ap = argparse.ArgumentParser(description = "Computing different convolutional operations on the specified images",
	epilog = "In the program folder you'll find a new folder named results. Go there and check some cool stuff!")

ap.add_argument("images", metavar = "IMAGES", type = str, help = "path to the images")

args = vars(ap.parse_args())
'''
	
# sharpen convolutional kernel	
def sharpen(path, name):

	img = cv2.imread(path)

	conv = np.matrix([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

	if img is None:
		raise Exception('can\'t open image, path might be wrong')

	conv_h, conv_w = conv.shape

	h = img.shape[0]
	w = img.shape[1]

	min_ind = -(conv_h/2)
	max_ind = (conv_w/2)+1

	limit_h = h
	limit_w = w

	final = np.zeros((h, w, 3), np.uint8)

	for x in xrange(h):
		for y in xrange(w):

			b, g, r = 0, 0, 0

			for xx in xrange(min_ind, max_ind):
				for yy in xrange(min_ind, max_ind):
					
					if x+xx >= limit_h or y+yy >= limit_w or x+xx < 0 or y+yy < 0:
						continue
					else:
						b = (b + (img.item(x+xx, y+yy, 0)*conv[xx+max_ind-1,yy+max_ind-1]))
						g = (g + (img.item(x+xx, y+yy, 1)*conv[xx+max_ind-1,yy+max_ind-1]))
						r = (r + (img.item(x+xx, y+yy, 2)*conv[xx+max_ind-1,yy+max_ind-1]))

			# blu pixel 
			final.itemset((x, y, 0), b)
			# green pixel
			final.itemset((x, y, 1), g)
			# red pixel
			final.itemset((x, y, 2), r)

	# adding 2pixel wide black frame to the image
	black_frame(final, h, w)

	# writing output
	cv2.imwrite("./results/conv/" + name +".png", final)

# aux method for adding 2pixel wide black frame to the image
def black_frame(output, h, w):

	output[0:2, :] = (0, 0, 0) 
	output[h-2:h, :] = (0, 0, 0) 
	output[:, 0:2] = (0, 0, 0) 
	output[: w-20:w] = (0, 0, 0) 

# aux method to calculate the right pixel value (weighted w/ each kernel element)
def compute(mat, conv, h, w):

	b, g, r = 0, 0, 0

	for x in xrange(h):	
		for y in xrange(w):

			b = b + (mat[x, y, 0]*conv[x, y])
			g = g + (mat[x, y, 1]*conv[x, y])
			r = r + (mat[x, y, 2]*conv[x, y])
			
	#return b, g, r
	return r,g,b

def filter_image(path):

	def work(matrix, name):

		img = cv2.imread(path)	

		conv = matrix

		# checkingh I could actually open the img
		if img is None:
			raise Exception('can\'t open image, path might be wrong')

		conv_h, conv_w = conv.shape

		h = img.shape[0]
		w = img.shape[1]

		# getting the min and max of the convolutional matrix (kernel)
		min_ind = -(conv_h/2)
		max_ind = (conv_w/2)+1

		# won't compute 2pixel wide border, setting a black frame instead
		limit_h = h
		limit_w = w

		final = np.zeros((h, w, 3), np.uint8)	

		for x in xrange(h):
			for y in xrange(w):
				if x+max_ind >= limit_h or y+max_ind >= limit_w or x+min_ind < 0 or y+min_ind < 0:
					continue
				else:
					mat = img[(x+min_ind):(x+max_ind), (y+min_ind):(y+max_ind)]

					#b, g, r  = compute(mat, conv, conv_h, conv_w)
					b, g, r  = compute(mat, conv, conv_h, conv_w)

				# blu pixel 
				final.itemset((x, y, 0), b)
				# green pixel
				final.itemset((x, y, 1), g)
				# red pixel
				final.itemset((x, y, 2), r)				

		# adding 2pixel wide black frame to the image
		black_frame(final, h, w)

		# writing output
		cv2.imwrite("./results/conv/" + name +".png", final)

	return work

#sharpen("./datasets/C.png", "sharpen")

x = filter_image("./datasets/try.png")

# edge detection
conv_edge_detection = np.matrix([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

# sharpen
conv_sharpen = np.matrix([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# gaussian blur
conv_gauss = np.matrix([[float(1)/16, float(1)/8, float(1)/16], [float(1)/8, float(1)/4, float(1)/8], [float(1)/16, float(1)/8, float(1)/16]])

# box blur
conv_blur = np.matrix([[float(1)/9, float(1)/9, float(1)/9], [float(1)/9, float(1)/9, float(1)/9], [float(1)/9, float(1)/9, float(1)/9]])

x(conv_edge_detection, "output")



