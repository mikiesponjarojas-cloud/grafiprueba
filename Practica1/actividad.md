# Actividad 1: Exploración del Espacio HSV

## Color seleccionado

Amarillo, rojo y verde.
v
---

## Código utilizado

```python
import cv2
import numpy as np

img = cv2.imread('frutas.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask_red = cv2.inRange(hsv, lower_red, upper_red)

mask = mask_green + mask_yellow + mask_red

result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen HSV", hsv)
cv2.imshow("Mascara", mask)
cv2.imshow("Resultado", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

Reflexión
¿Qué ocurre cuando el rango es muy estrecho?

Cuando el rango es muy estrecho, la máscara no detecta completamente el objeto, ya que algunos tonos quedan fuera del rango.

¿Qué ocurre cuando el rango es muy amplio?

Cuando el rango es muy amplio, la máscara detecta colores que no pertenecen al objeto, incluyendo el fondo.