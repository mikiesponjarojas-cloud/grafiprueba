import cv2
import numpy as np




img = np.random.randint(0, 256, (300, 700, 3), dtype=np.uint8)

# Texto 
texto = "CLAVE-DELTA"

# Dibujar texto en VERDE fuerte 
cv2.putText(img, texto, (50, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            2, (0, 255, 0), 5)  # B=0, G=255, R=0


cv2.imwrite("m5_tricolor.png", img)



# Separar canales
b, g, r = cv2.split(img)


solo_b = b
solo_g = g
solo_r = r


diff_gb = cv2.absdiff(g, b)


norm = cv2.normalize(diff_gb, None, 0, 255, cv2.NORM_MINMAX)


_, mask = cv2.threshold(norm, 50, 255, cv2.THRESH_BINARY)


cv2.imwrite("m5_mensaje.png", mask)


# Mostrar resultados

cv2.imshow("Original", img)
cv2.imshow("Canal G", solo_g)
cv2.imshow("Diff G-B", diff_gb)
cv2.imshow("Mensaje Recuperado", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()