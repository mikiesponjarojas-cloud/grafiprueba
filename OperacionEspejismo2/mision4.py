import cv2
import numpy as np


img = cv2.imread("OperacionEspejismo2/m4_ruido.png")

if img is None:
    print("Error cargando imagen")
    exit()

# Kernel promedio 3x3
kernel = np.ones((3, 3), np.float32) / 9

# Aplicar convolución 
suavizada = cv2.filter2D(img, -1, kernel)


cv2.imwrite("m4_suavizada.png", suavizada)

# Convertir a HSV
hsv = cv2.cvtColor(suavizada, cv2.COLOR_BGR2HSV)

#Rango para CYAN (ajustable si falla)
lower_cyan = np.array([80, 100, 100])
upper_cyan = np.array([100, 255, 255])

# Crear máscara
mask = cv2.inRange(hsv, lower_cyan, upper_cyan)

# Guardar máscara
cv2.imwrite("m4_mask_cyan.png", mask)

# Mostrar resultados
cv2.imshow("Original", img)
cv2.imshow("Suavizada", suavizada)
cv2.imshow("Mascara Cyan", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()