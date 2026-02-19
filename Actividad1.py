import cv2
import numpy as np

# Leer la imagen
img = cv2.imread('C:\\Users\\mikie\\Desktop\\Universidad\\Fondos4k\\frutas.png')

# Convertir la imagen al espacio de color HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Rango verde
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

# Rango amarillo
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

# Rango rojo
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# Crear máscaras
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask_red = cv2.inRange(hsv, lower_red, upper_red)

# Unir máscaras
mask = mask_green + mask_yellow + mask_red

# Aplicar máscara
result = cv2.bitwise_and(img, img, mask=mask)

# Mostrar imágenes
cv2.imshow("Imagen Original", img)

cv2.imshow("Imagen HSV", hsv)   # 👈 iamgen

cv2.imshow("Mascara", mask)     # 👈 mascara

cv2.imshow("Color Detectado", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
