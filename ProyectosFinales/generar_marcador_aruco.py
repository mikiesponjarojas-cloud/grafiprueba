import cv2
import numpy as np

# Diccionario ArUco
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

# Generar marcador
if hasattr(cv2.aruco, "generateImageMarker"):
    img = cv2.aruco.generateImageMarker(dictionary, 0, 400)
else:
    img = cv2.aruco.drawMarker(dictionary, 0, 400)

# Fondo blanco
canvas = np.full((480, 480), 255, np.uint8)
canvas[40:440, 40:440] = img

# Guardar imagen
cv2.imwrite("marcador_aruco_id0.png", canvas)

print("Imagen guardada correctamente")