# This is file 46.py

import cv2

image = cv2.imread("/Users/tripurakant/Documents/Imp-folder/py/Python-Scripting/250questions/image.jpg",
                   cv2.IMREAD_UNCHANGED)
cv2.imshow("title", image)

cv2.waitKey(0)
