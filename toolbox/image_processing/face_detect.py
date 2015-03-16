""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("/home/ian/Dropbox/2014-2015/Ubuntu/SoftDesSp15/toolbox/image_processing/haarcascade_frontalface_alt.xml")
kernel = np.ones((21, 21), "uint8")

while(True):
	ret, frame = cam.read()
	faces  = face_cascade.detectMultiScale(frame, scaleFactor = 1.2, minSize = (20, 20))
	for (x, y , w, h) in faces:
		frame[y: y + h, x: x + w, :] = cv2.dilate(frame[y: y + h, x: x + w, :], kernel)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255))
		cv2.ellipse(frame, (x + w/2, y + 3 * h/4), (60, 20), 0, 180, 0, (0, 0, 0), 10)
		cv2.circle(frame, (x + 5 * w/16, y + h/3), 3, (0, 0, 0), 10)
		cv2.circle(frame, (x + 11 * w/16, y + h/3), 3, (0, 0, 0), 10)

	cv2.imshow("frame", frame)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

cam.release()
cv2.destroyAllWindows()