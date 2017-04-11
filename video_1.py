# USE ctrl-c to exit

import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
bgst = cv2.createBackgroundSubtractorMOG2()
fourcc=cv2.VideoWriter_fourcc(*'DIVX') 

win = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter( "Record.avi", fourcc, 16, win )

while (cap.isOpened()):
	ret, frame = cap.read()
	dst = bgst.apply(frame)
	dst = np.array(dst, np.int8)

    
	if np.count_nonzero(dst)>30000:

		print('Recording')
		out.write(frame)
	
	else:
		print("Not Recording")



