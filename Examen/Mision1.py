import cv2
import numpy as np

#  escala de grises
img = cv2.imread('Examen/m1_oscura.png', cv2.IMREAD_GRAYSCALE)


# --- MODO RAW  ---


# Obtener dimensiones
alto, ancho = img.shape

# Crear una copia 
img_raw = img.copy()

# Recorrer cada pixel con ciclos
for i in range(alto):
    for j in range(ancho):

        # Multiplicar por 50
        nuevo_valor = img_raw[i, j] * 50

        # Evitar que supere 255
        nuevo_valor = np.clip(nuevo_valor, 0, 255)

        
        img_raw[i, j] = nuevo_valor

# --- MODO OPENCV  ---


# Multiplicación vectorizada
img_opencv = img * 50

# Limitar valores entre 0 y 255
img_opencv = np.clip(img_opencv, 0, 255).astype(np.uint8)



cv2.imshow("Imagen Original Oscura", img)
cv2.imshow("Resultado Modo RAW", img_raw)
cv2.imshow("Resultado OpenCV", img_opencv)

cv2.waitKey(0)
cv2.destroyAllWindows()