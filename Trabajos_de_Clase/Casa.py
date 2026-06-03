import cv2
import numpy as np

# Lienzo
img = np.ones((500, 700, 3), dtype=np.uint8) * 255


# FRENTE DE LA CASA


# Cuadrado frontal
cv2.line(img, (200, 300), (400, 300), (0, 0, 0), 2)
cv2.line(img, (200, 300), (200, 180), (0, 0, 0), 2)
cv2.line(img, (400, 300), (400, 180), (0, 0, 0), 2)
cv2.line(img, (200, 180), (400, 180), (0, 0, 0), 2)

# Techo frontal
cv2.line(img, (200, 180), (300, 100), (0, 0, 0), 2)
cv2.line(img, (300, 100), (400, 180), (0, 0, 0), 2)

#Profundidad

offset = 100  # profundidad

# Parte trasera (desplazada)
cv2.line(img, (200+offset, 300-offset), (400+offset, 300-offset), (0, 0, 0), 2)
cv2.line(img, (200+offset, 300-offset), (200+offset, 180-offset), (0, 0, 0), 2)
cv2.line(img, (400+offset, 300-offset), (400+offset, 180-offset), (0, 0, 0), 2)
cv2.line(img, (200+offset, 180-offset), (400+offset, 180-offset), (0, 0, 0), 2)

# Techo trasero
cv2.line(img, (200+offset, 180-offset), (300+offset, 100-offset), (0, 0, 0), 2)
cv2.line(img, (300+offset, 100-offset), (400+offset, 180-offset), (0, 0, 0), 2)


# CONEXIONES 


# Unir esquinas
cv2.line(img, (200, 300), (200+offset, 300-offset), (0, 0, 0), 2)
cv2.line(img, (400, 300), (400+offset, 300-offset), (0, 0, 0), 2)
cv2.line(img, (200, 180), (200+offset, 180-offset), (0, 0, 0), 2)
cv2.line(img, (400, 180), (400+offset, 180-offset), (0, 0, 0), 2)

# Conectar techo
cv2.line(img, (300, 100), (300+offset, 100-offset), (0, 0, 0), 2)


# PUERTA (frente)


cv2.line(img, (270, 300), (270, 230), (0, 0, 0), 2)
cv2.line(img, (330, 300), (330, 230), (0, 0, 0), 2)
cv2.line(img, (270, 230), (330, 230), (0, 0, 0), 2)


# VENTANA LATERAL 


# Ventana en cara derecha
cv2.line(img, (400, 240), (450, 200), (0, 0, 0), 2)
cv2.line(img, (450, 200), (450, 250), (0, 0, 0), 2)
cv2.line(img, (450, 250), (400, 290), (0, 0, 0), 2)
cv2.line(img, (400, 290), (400, 240), (0, 0, 0), 2)


# SUELO 


for i in range(0, 200, 20):
    cv2.line(img, (150+i, 350), (250+i, 300), (0, 0, 0), 1)



cv2.imshow("Casa 3D con Lineas", img)
cv2.waitKey(0)
cv2.destroyAllWindows()