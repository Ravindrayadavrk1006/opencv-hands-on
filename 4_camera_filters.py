import cv2
import sys
camera_no = 0
#if we want to read from some other camera
if len(sys.argv)>1:
    camera_no = sys.argv[1]
device = cv2.VideoCapture(camera_no)
window = cv2.namedWindow('camera_filter')


while True:
    #read the frame from the camera
    is_frame, frame = device.read()
    if not is_frame:
        break
    