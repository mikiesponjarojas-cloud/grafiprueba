import cv2 as cv
import numpy as np

img = np.ones((400, 400), np.uint8) * 255

for i in range(256):
    for j in range(256):
        img[i, j] = 255 - j

cv.imshow("Degradado", img)
cv.waitKey(0)
cv.destroyAllWindows()
