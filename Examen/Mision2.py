import cv2
import numpy as np


mitad1 = cv2.imread('Examen/m2_mitad1.png')
mitad2 = cv2.imread('Examen/m2_mitad2.png')

# lienzo negro de 400x400
lienzo = np.zeros((400,400,3), dtype=np.uint8)


# 2 TRASLADAR MITAD 1


h1, w1 = mitad1.shape[:2]

# matriz de traslación
M_trans = np.float32([
    [1,0,-50],   #  X
    [0,1,-50]    #  Y
])

mitad1_corregida = cv2.warpAffine(mitad1, M_trans, (400,400))

# colocar en el lienzo (superior)
lienzo[0:h1, 0:w1] = mitad1_corregida[0:h1, 0:w1]


# 3ROTAR MITAD 2


h2, w2 = mitad2.shape[:2]

# centro de rotación
centro = (w2//2, h2//2)

# matriz de rotación 180 grados
M_rot = cv2.getRotationMatrix2D(centro, 180, 1)

mitad2_rotada = cv2.warpAffine(mitad2, M_rot, (w2,h2))

# parte inferior
lienzo[200:200+h2, 0:w2] = mitad2_rotada




cv2.imshow("Mitad 1", mitad1)
cv2.imshow("Mitad 2", mitad2)
cv2.imshow("QR reconstruido", lienzo)

cv2.waitKey(0)
cv2.destroyAllWindows()