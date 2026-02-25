import cv2 as cv
import numpy as np 

img = np.ones((500,500), np.uint8)*150 

cv.circle(img, (250,200), 30, (0, 255, 255), -1)

cv.circle(img, (250,140), 30, (255, 0, 255), -1)
cv.circle(img, (250,260), 30, (255, 0, 255), -1)
cv.circle(img, (190,200), 30, (255, 0, 255), -1)
cv.circle(img, (310,200), 30, (255, 0, 255), -1)






  




cv.imshow('Flor', img)
cv.waitKey(0)
cv.destroyAllWindows()