import numpy as np 
import cv2

# capturing from camera
cap = cv2.VideoCapture(0)

print 'dimension: hXw = '
print cap.get(3), cap.get(4)

#fourcc = cv2.VideoWriter_fourcc(*'avc1')
fourcc = cv2.cv.CV_FOURCC(*'mp4v')
out = cv2.VideoWriter('output.avi', fourcc, 24.0, (1280, 720))

if not cap.isOpened():
	
	#from camera
	cap.open(0)

else:
	while(cap.isOpened()):
		ret, frame = cap.read()

		if ret == True:
			frame = cv2.flip(frame, 2)
			# converting to black&white
			#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			out.write(frame)

			cv2.imshow('frame', frame)

			if cv2.waitKey(1) == ord('q'):
				break

		else:
			break

cap.release()
out.release()
cv2.destroyAllWindows()
