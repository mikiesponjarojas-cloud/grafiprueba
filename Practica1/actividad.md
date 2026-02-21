# UNIVERSIDAD

## Materia: **Graficación**

---

# **Actividad: Exploración del Espacio de Color HSV**

---

**Alumno:** Miguel Rojas Santillan
**Materia:** Graficación
**Profesor:** _______________________
**Fecha:** _______________________

---

# Índice

1. Actividad 1: Exploración del Espacio HSV
2. Actividad 2: Limpieza de Ruido
3. Actividad 3: Conteo de Regiones
4. Actividad 4: Comparación entre los colores
5. Actividad 5: Análisis Crítico
6. Capturas

---

# Actividad 1: Exploración del Espacio HSV

## Color seleccionado

Los colores seleccionados fueron:

* Verde
* Amarillo
* Rojo

Estos colores fueron elegidos para identificar frutas dentro de una imagen utilizando el espacio de color HSV.

---

## Código utilizado

```python
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
```

---

## Pregunta

### ¿Qué ocurre cuando el rango es muy amplio?

Cuando el rango es muy amplio, la máscara detecta no solamente el objeto deseado, sino también otros elementos del fondo que tienen colores similares. Esto provoca errores en la segmentación y disminuye la precisión del resultado.

---

# Actividad 2: Limpieza de Ruido

## Código utilizado

(Agregar codigo)

---

## Preguntas

### ¿Qué tipo de ruido aparece?

Aparece ruido tipo puntos pequeños o regiones aisladas que no pertenecen al objeto real. Este ruido es causado por variaciones de iluminación o similitud de colores en el fondo.

---

### ¿Por qué es necesario eliminarlo antes del conteo?

Porque el ruido puede ser detectado como objetos adicionales, generando un conteo incorrecto.

Eliminar el ruido permite obtener resultados más precisos.

---

# Actividad 3: Conteo de regiones

(Agregar codigo)

En esta actividad se cuentan las frutas detectadas utilizando las máscaras.

---

# Actividad 4: Comparación entre los colores

En esta actividad se comparó el comportamiento de cada color detectado.

---

## Preguntas

### ¿Qué color fue más fácil?

El color verde fue más fácil de detectar porque tiene un rango más definido en HSV.

---

### ¿Cuál presentó más ruido?

El color rojo presentó más ruido.

---

### ¿Por qué?

Porque el rojo se encuentra dividido en dos rangos dentro del espacio HSV, lo que hace la detección más compleja.

---

# Actividad 5: Análisis Crítico

## Preguntas

---

### 1. ¿Por qué HSV es más adecuado que RGB para esta tarea?

Porque HSV separa el color de la iluminación, lo que facilita detectar colores específicos.

---

### 2. ¿Cómo afecta la iluminación?

La iluminación afecta principalmente el canal V (valor), cambiando el brillo del objeto.

---

### 3. ¿Qué sucede si dos frutas tienen tonos similares?

El sistema puede confundirlas y detectarlas como el mismo objeto.

---

### 4. ¿Qué limitaciones tiene la segmentación por color?

* Sensible a la iluminación
* Puede detectar objetos incorrectos
* No distingue forma
* No distingue textura

---

# Capturas

Agregar aquí:

* Imagen original
* Imagen verde
* Imagen rojo
* Imagen amarillo

---

# Conclusión

El espacio de color HSV facilita la detección de colores específicos en imágenes. Sin embargo, es necesario ajustar correctamente los rangos y eliminar el ruido para obtener resultados precisos.

Esta técnica es útil en visión artificial para el reconocimiento de objetos.

---





