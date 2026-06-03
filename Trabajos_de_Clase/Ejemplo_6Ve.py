import cv2
import numpy as np

# Leer la imagen
img = cv2.imread("C:\\Users\\mikie\\Desktop\\Universidad\\Fondos4k\\Manzana.jpg")

# Convertir la imagen al espacio de color HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Definir el rango inferior y superior para detectar verde
lower_green = np.array([0, 100, 100])  # Hue, Saturación, Brillo mínimos
upper_green = np.array([10, 255, 255])  # Hue, Saturación, Brillo máximos

lower_green = np.array([170, 100, 100])  # Hue, Saturación, Brillo mínimos
upper_green = np.array([180, 255, 255])  # Hue, Saturación, Brillo máximos



# Crear una máscara que solo incluya los píxeles dentro del rango
mask1 = cv2.inRange(hsv, lower_green, upper_green)
mask2 = cv2.inRange(hsv, lower_green, upper_green)

mask = mask1 +  mask2


# Aplicar la máscara a la imagen original
result = cv2.bitwise_and(img, img, mask=mask)

# Mostrar la imagen original y la imagen con el color detectado
cv2.imshow("mascara", mask)

cv2.imshow("Imagen Original", img)
cv2.imshow("Color Detectado", result)
cv2.waitKey(0)
cv2.destroyAllWindows()