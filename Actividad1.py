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

#Crear mascaras
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Aplicar máscara
result_green = cv2.bitwise_and(img,img, mask=mask_green)
result_red = cv2.bitwise_and(img,img,mask=mask_red )
result_yellow = cv2.bitwise_and(img,img,mask=mask_yellow )



# Mostrar imágenes
cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen HSV", hsv)   
#Colores
cv2.imshow("Color Detectado Verde", result_green)
cv2.imshow("Color Detectado Rojo", result_red)
cv2.imshow("Color Detectado Amarillo ", result_yellow)



cv2.waitKey(0)
cv2.destroyAllWindows()
