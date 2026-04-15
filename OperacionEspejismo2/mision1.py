import cv2
import numpy as np

img = cv2.imread("OperacionEspejismo2/m1_oscura 1.png", cv2.IMREAD_GRAYSCALE)
h, w = img.shape

# Crear matriz 
recuperado = np.zeros((h, w), dtype=np.int32)

#multiplicar por 50
for y in range(h):
    for x in range(w):
        recuperado[y, x] = img[y, x] * 50

#Convertir
recuperado = np.clip(recuperado, 0, 255)
recuperado_uint8 = recuperado.astype(np.uint8)

cv2.imwrite("m1_recuperado_x50.png", recuperado_uint8)

recuperado2 = np.zeros((h, w), dtype=np.int32)

#Sumar +20
for y in range(h):
    for x in range(w):
        recuperado2[y, x] = recuperado_uint8[y, x] + 20

#Convertir
recuperado2 = np.clip(recuperado2, 0, 255)
recuperado2_uint8 = recuperado2.astype(np.uint8)

cv2.imwrite("m1_recuperado_x50_mas20.png", recuperado2_uint8)

vectorizado = np.clip(img * 50 + 20, 0, 255).astype(np.uint8)

cv2.imwrite("m1_vectorizado.png", vectorizado)

#Resultados
cv2.imshow("Original", img)
cv2.imshow("x50", recuperado_uint8)
cv2.imshow("x50 + 20", recuperado2_uint8)
cv2.imshow("Vectorizado", vectorizado)

cv2.waitKey(0)
cv2.destroyAllWindows()