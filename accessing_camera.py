import cv2
import sys

#we will be using the default camera
camera_no = 0
#if we want to read from some other camera then we can pass that value
if len(sys.argv) > 1:
    camera_no = int(sys.argv[1])  # Convert to integer

#creating a video capture object
device = cv2.VideoCapture(camera_no)

if not device.isOpened():  # Check if the camera opened successfully
    print(f"Error: Unable to access camera {camera_no}")
    sys.exit(1)

#creating a window to show the video

window = cv2.namedWindow('default', cv2.WINDOW_AUTOSIZE)

#until someone doesn't press the escape key
while True:
    has_frame, frame  = device.read()
    if not has_frame:
        print("Error: Unable to read frame from camera")
        break
    cv2.imshow('default', frame)
    if cv2.waitKey(1) == 27:  # Exit on ESC key
        break

device.release()
cv2.destroyAllWindows()  # Destroy all windows