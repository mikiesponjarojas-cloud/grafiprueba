import cv2
import numpy as np

# Cargar la imagen
img_microfilm = cv2.imread('Mision3/microfilm.jpg')

# Recorte central
recorte = img_microfilm[900:1100, 900:1100]


# MÉTODO 1: MODO RAW (Vecino más cercano manual)


h, w, c = recorte.shape
scale = 5

nuevo_h = h * scale
nuevo_w = w * scale

lienzo = np.zeros((nuevo_h, nuevo_w, c), dtype=np.uint8)

for y in range(nuevo_h):
    for x in range(nuevo_w):
        orig_x = int(x / scale)
        orig_y = int(y / scale)
        lienzo[y, x] = recorte[orig_y, orig_x]

cv2.imwrite("escalado_raw.jpg", lienzo)


# MÉTODO 2: MODO OPENCV (Interpolación)


escalado_opencv = cv2.resize(
    recorte,
    None,
    fx=5,
    fy=5,
    interpolation=cv2.INTER_CUBIC
)

cv2.imwrite("escalado_opencv.jpg", escalado_opencv)

# Mostrar resultados
cv2.imshow("Recorte", recorte)
cv2.imshow("Escalado RAW", lienzo)
cv2.imshow("Escalado OpenCV", escalado_opencv)

cv2.waitKey(0)
cv2.destroyAllWindows()