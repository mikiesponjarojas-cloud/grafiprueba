import cv2 as cv
import numpy as np 

img = np.ones((500,500), np.uint8)*150 

cv.circle(img, (250,200), 30, (0, 255, 255), -1)

cv.circle(img, (250,140), 30, (255, 0, 255), -1)
cv.circle(img, (250,260), 30, (255, 0, 255), -1)
cv.circle(img, (190,200), 30, (255, 0, 255), -1)
cv.circle(img, (310,200), 30, (255, 0, 255), -1)

cv.line(img, (250,230), (250,400), (0,255,0), 5)

# Hoja izquierda
cv.circle(img, (220,300), 20, (0,255,0), -1)

# Hoja derecha
cv.circle(img, (280,350), 20, (0,255,0), -1)

cv.imshow('Flor', img)
cv.waitKey(0)
cv.destroyAllWindows()