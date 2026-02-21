import cv2
import numpy as np

# Leer la imagen
img = cv2.imread('C:\\Users\\mikie\\Desktop\\Universidad\\Fondos4k\\frutas.png')

# Convertir la imagen al espacio de color HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Rango de colores verde, amarillo, rojo

lower_green = np.array([35, 80, 80])
upper_green = np.array([85, 255, 255])

lower_yellow = np.array([20, 120, 120])
upper_yellow = np.array([35, 255, 255])

lower_red1 = np.array([0, 120, 120])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 120, 120])
upper_red2 = np.array([180, 255, 255])


# Crear mascaras
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Unir rojos
mask_red = mask_red1 + mask_red2

# Aplicar máscara
result_green = cv2.bitwise_and(img,img, mask=mask_green)
result_red = cv2.bitwise_and(img,img, mask=mask_red)
result_yellow = cv2.bitwise_and(img,img, mask=mask_yellow)

# Mostrar imágenes
cv2.imshow("Imagen Original", img)
cv2.imshow("Color Detectado Verde", result_green)
cv2.imshow("Color Detectado Rojo", result_red)
cv2.imshow("Color Detectado Amarillo", result_yellow)

cv2.waitKey(0)
cv2.destroyAllWindows()