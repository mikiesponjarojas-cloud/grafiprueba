import cv2  as cv 
import numpy as np


img = cv.imread("C:\\Users\\mikie\\Desktop\\Universidad\\Fondos4k\\1384649.jpg", 0)
print (img.shape)

cv.imshow('img', img)
cv.waitKey()
cv.destroyAllwindows() 