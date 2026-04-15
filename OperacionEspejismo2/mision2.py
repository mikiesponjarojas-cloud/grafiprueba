import cv2
import numpy as np


mitad1 = cv2.imread("OperacionEspejismo2/m2_mitad1.png")
mitad2 = cv2.imread("OperacionEspejismo2/m2_mitad2.png")


if mitad1 is None or mitad2 is None:
    print("Error cargando imágenes")
    exit()

#Lienzo blanco 400x400
lienzo = np.full((400, 400, 3), 255, dtype=np.uint8)

h1, w1 = mitad1.shape[:2]
h2, w2 = mitad2.shape[:2]



#Inversa
dx = -50   # mover izquierda
dy = -30   # mover arriba

M_tras = np.float32([
    [1, 0, dx],
    [0, 1, dy]
])

mitad1_corregida = cv2.warpAffine(mitad1, M_tras, (w1, h1))

#Centrado
x_offset = (400 - w1) // 2
lienzo[0:h1, x_offset:x_offset+w1] = mitad1_corregida




# Centro de la imagen
centro = (w2 // 2, h2 // 2)

M_rot = cv2.getRotationMatrix2D(centro, 180, 1)

mitad2_corregida = cv2.warpAffine(mitad2, M_rot, (w2, h2))

#Parte inferior 
x_offset2 = (400 - w2) // 2
lienzo[400-h2:400, x_offset2:x_offset2+w2] = mitad2_corregida



cv2.imwrite("m2_qr_reconstruido.png", lienzo)


#Resultados
cv2.imshow("QR reconstruido", lienzo)
cv2.waitKey(0)
cv2.destroyAllWindows()