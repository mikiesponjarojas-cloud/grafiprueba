import cv2
import numpy as np


#Crear lienzo azul oscuro


# (alto, ancho, canales)
lienzo = np.full((500,500,3), (50,20,20), dtype=np.uint8)


#  Dibujar círculo amarillo


cv2.circle(
    lienzo,
    (250,250),     
    100,           
    (0,255,255),   
    3              
)


#  Rectángulo rojo sólido


cv2.rectangle(
    lienzo,
    (200,200),     
    (300,300),     
    (0,0,255),     
    -1             
)


# Líneas blancas en X


cv2.line(
    lienzo,
    (0,0),
    (500,500),
    (255,255,255),
    2
)

cv2.line(
    lienzo,
    (500,0),
    (0,500),
    (255,255,255),
    2
)



cv2.imshow("Sello Biometrico", lienzo)

cv2.imwrite("m3_sello_forjado.png", lienzo)

cv2.waitKey(0)
cv2.destroyAllWindows()