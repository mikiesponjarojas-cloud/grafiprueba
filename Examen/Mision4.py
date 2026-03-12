import cv2
import numpy as np


img = cv2.imread('Examen/m4_ruido.png')

#Convertir a HSV

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# Definir rango Cyan


bajo = np.array([80,100,100])
alto = np.array([100,255,255])


#  Crear máscara

mascara = cv2.inRange(hsv, bajo, alto)


cv2.imshow("Imagen original", img)
cv2.imshow("Mascara Cyan", mascara)

cv2.waitKey(0)
cv2.destroyAllWindows()