import cv2
import numpy as np
import math


#Crear lienzo negro 500x500


lienzo = np.zeros((500,500,3), dtype=np.uint8)

# Recorrer t


t = 0

while t <= 2 * math.pi:

#Calcular ecuaciones
    x = 250 + 150 * math.sin(3 * t)
    y = 250 + 150 * math.sin(2 * t)

    # convertir a enteros
    x = int(x)
    y = int(y)

  
    #Dibujar punto


    cv2.circle(lienzo, (x,y), 1, (255,255,255), -1)

    t += 0.01



cv2.imshow("Antena Parabolica", lienzo)

cv2.waitKey(0)
cv2.destroyAllWindows()