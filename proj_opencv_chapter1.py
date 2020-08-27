'''title: OpenCV (Computer Vision)
reference1: 
    "Learn OpenCV in 3 hours" Murtaza's Workshop on: Youtube
dependencies: 
    Python 3.7.6
    pip install opencv-python (aimed at real-time computer vision)
'''

import cv2
print("Package imported")

#reading an image (.png image stored in same folder as this python file)
#img = cv2.imread("lenna.jpg")
img = cv2.imread("lena.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0) #0 means image will be shown indefinitely

