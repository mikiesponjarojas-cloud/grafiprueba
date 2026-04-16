import cv2
import numpy as np
import math

img = np.zeros((600, 600, 3), dtype=np.uint8)
img[:] = (40, 20, 20)

# Centro
cx, cy = 300, 300

# 1️Círculo exterior amarillo
cv2.circle(img, (cx, cy), 170, (0, 255, 255), 3)

# 2️Círculo interior amarillo
cv2.circle(img, (cx, cy), 110, (0, 255, 255), 2)

# 3️Rectángulo rojo relleno
cv2.rectangle(img, (250, 260), (350, 340), (0, 0, 255), -1)

#Diagonales blancas (X)
cv2.line(img, (0, 0), (600, 600), (255, 255, 255), 2)
cv2.line(img, (600, 0), (0, 600), (255, 255, 255), 2)

# 5️círculos verdes alrededor 
radio = 140
for i in range(8):
    angulo = i * (2 * math.pi / 8)
    x = int(cx + radio * math.cos(angulo))
    y = int(cy + radio * math.sin(angulo))
    cv2.circle(img, (x, y), 8, (0, 255, 0), -1)

# Texto 
texto = "SECTOR-9"
font = cv2.FONT_HERSHEY_SIMPLEX
escala = 1
grosor = 2

(t_w, t_h), _ = cv2.getTextSize(texto, font, escala, grosor)
x_texto = (600 - t_w) // 2
y_texto = 560

cv2.putText(img, texto, (x_texto, y_texto), font, escala, (255, 255, 255), grosor)


cv2.imwrite("m3_sello_forjado_v2.png", img)

# Mostrar resultado
cv2.imshow("Sello Biométrico II", img)
cv2.waitKey(0)
cv2.destroyAllWindows()