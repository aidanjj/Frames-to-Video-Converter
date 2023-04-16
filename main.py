import cv2
import numpy as np

framecount = 100
filepath = ''
videoWidth = 1920
videoHeight = 1080

fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter('001.avi',cv2.VideoWriter_fourcc(*'MJPG'),60, (videoWidth,videoHeight))

for i in range(1,framecount):
    img = cv2.imread(filepath + '/img' + str(i) + '.png')
    out.write(img)

cv2.destroyAllWindows()

out.release()
