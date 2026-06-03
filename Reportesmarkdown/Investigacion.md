<div align="center">

---

# Tecnológico de Morelia

## Instituto Tecnológico de Morelia

---

**Materia:** Graficación

**Tema:** Algoritmos de Puntos Característicos aplicados a la Realidad Aumentada y el Aprendizaje Máquina

---

**Alumno:** Miguel Rojas Santillán

**Profesor:** Jesús Eduardo Alcaraz Chávez

**Fecha:** Mayo 2025

---

</div>

---

## Índice

1. [Introducción](#introducción)
2. [¿Qué son los puntos característicos?](#qué-son-los-puntos-característicos)
3. [SIFT](#sift)
4. [SURF](#surf)
5. [ORB](#orb)
6. [Comparativa](#comparativa)
7. [Aplicación en Realidad Aumentada](#aplicación-en-realidad-aumentada)
8. [Relación con Machine Learning](#relación-con-machine-learning)
9. [Conclusiones](#conclusiones)
10. [Referencias](#referencias)

---

## Introducción

Los **algoritmos de puntos característicos** son fundamentales en visión por computadora. Permiten identificar regiones únicas en una imagen para compararlas con otras, lo cual es esencial en aplicaciones de **Realidad Aumentada (AR)** y **Aprendizaje Máquina (ML)**.

Los tres algoritmos más utilizados son SIFT, SURF y ORB. Cada uno tiene un enfoque distinto en términos de precisión, velocidad y licencia de uso.

---

## ¿Qué son los puntos característicos?

Un **punto característico** (keypoint) es una región de una imagen que:

- Es **distinguible** frente a su entorno
- Se puede **detectar de forma repetible** ante cambios de escala, rotación o iluminación
- Puede ser **descrita matemáticamente** mediante un vector (descriptor)

El proceso general es:

```
Imagen → Detección de keypoints → Cálculo del descriptor → Emparejamiento
```

---

## SIFT

**Scale-Invariant Feature Transform** — David Lowe, 2004

SIFT detecta puntos estables en múltiples escalas usando el operador **Difference of Gaussians (DoG)** y genera un descriptor de **128 dimensiones** basado en histogramas de gradiente.

**Ventajas:**
- Alta precisión y robustez
- Invariante a escala, rotación e iluminación

**Desventajas:**
- Lento (no apto para tiempo real sin GPU)
- Descriptor de alta dimensionalidad

---

## SURF

**Speeded-Up Robust Features** — Bay et al., 2006

SURF es una versión más rápida de SIFT que usa **imágenes integrales** y filtros de caja para aproximar las segundas derivadas. Genera un descriptor de **64 dimensiones**.

**Ventajas:**
- 2-3× más rápido que SIFT
- Buena robustez ante escala y rotación

**Desventajas:**
- Algoritmo patentado (uso comercial requiere licencia)
- Menos preciso que SIFT en condiciones difíciles

---

## ORB

**Oriented FAST and Rotated BRIEF** — Rublee et al., 2011

ORB combina el detector **FAST** (muy rápido para encontrar esquinas) con el descriptor binario **BRIEF**, al cual le añade invariancia a rotación. El descriptor tiene **256 bits** y el emparejamiento se realiza con la distancia de Hamming.

**Ventajas:**
- Extremadamente rápido (~100× más que SIFT)
- Libre de patentes, incluido en OpenCV sin costo
- Ideal para dispositivos móviles y AR en tiempo real

**Desventajas:**
- Menos robusto ante cambios grandes de escala
- Mayor sensibilidad a variaciones de iluminación

---

## Comparativa

| Característica        | SIFT        | SURF        | ORB              |
|-----------------------|-------------|-------------|------------------|
| Velocidad             | Lenta       | Media       | Muy rápida       |
| Precisión             | Alta        | Media-alta  | Media            |
| Licencia              | Libre       | Patentado   | Libre (Apache 2) |
| Tamaño del descriptor | 128 floats  | 64 floats   | 256 bits         |
| Uso en tiempo real    | No          | Posible     | Sí               |
| Uso recomendado       | Investigación | Aplicaciones con GPU | Móvil / AR |

---

## Aplicación en Realidad Aumentada

En AR, los puntos característicos permiten detectar y rastrear imágenes del mundo real para **anclar contenido digital** sobre ellas sin necesidad de marcadores cuadrados.

**Flujo general:**

```
1. Cargar imagen de referencia (marcador)
2. Detectar keypoints y calcular descriptores
3. Capturar frame de la cámara en tiempo real
4. Detectar keypoints en el frame
5. Emparejar descriptores (con RANSAC para filtrar ruido)
6. Calcular homografía (transformación entre planos)
7. Estimar pose de la cámara (PnP)
8. Renderizar objeto 3D sobre la escena
```

**Ejemplo básico con ORB en Python:**

```python
import cv2
import numpy as np

orb = cv2.ORB_create(500)
marker = cv2.imread('marcador.jpg', cv2.IMREAD_GRAYSCALE)
kp_m, des_m = orb.detectAndCompute(marker, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp_f, des_f = orb.detectAndCompute(gray, None)
    if des_f is not None:
        matches = sorted(bf.match(des_m, des_f), key=lambda x: x.distance)
        if len(matches) > 10:
            # Calcular homografía y proyectar contenido AR
            pass
    cv2.imshow('AR', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

---

## Relación con Machine Learning

Los puntos característicos se integran con ML de dos formas principales:

**1. Bag of Visual Words (BoVW)**
Los descriptores se agrupan con K-Means para crear un "vocabulario visual". Cada imagen se representa como un histograma de palabras visuales, que se usa para entrenar clasificadores como SVM o redes neuronales.

**2. Descriptores aprendidos con redes neuronales**
Métodos modernos como **SuperPoint** (2018) y **LightGlue** (2023) aprenden a detectar y describir puntos mediante CNN, superando en precisión a los métodos clásicos en escenas complejas.

| Método        | Tipo        | Precisión | Velocidad |
|---------------|-------------|-----------|-----------|
| SIFT / SURF   | Clásico     | Alta      | Baja      |
| ORB           | Clásico     | Media     | Muy alta  |
| SuperPoint    | Deep Learning | Muy alta | Media    |
| LightGlue     | Deep Learning | Muy alta | Alta     |

---

## Conclusiones

- **SIFT** es el estándar de referencia en investigación por su alta precisión.
- **SURF** ofrece una mejora de velocidad, pero su uso está limitado por la patente.
- **ORB** es la opción más práctica para aplicaciones AR en tiempo real por ser rápido, gratuito y eficiente en móviles.
- Los métodos basados en **Deep Learning** (SuperPoint, LightGlue) representan el futuro de la detección de puntos, especialmente en condiciones difíciles.

Para un proyecto de Realidad Aumentada en Graficación, **ORB con OpenCV** es el punto de partida recomendado por su facilidad de implementación y rendimiento.

---

## Referencias

1. Lowe, D. G. (2004). *Distinctive Image Features from Scale-Invariant Keypoints*. IJCV, 60(2).
2. Bay, H., Tuytelaars, T., & Van Gool, L. (2006). *SURF: Speeded Up Robust Features*. ECCV.
3. Rublee, E. et al. (2011). *ORB: An efficient alternative to SIFT or SURF*. ICCV.
4. DeTone, D. et al. (2018). *SuperPoint: Self-Supervised Interest Point Detection*. CVPR Workshops.
5. OpenCV Documentation: https://docs.opencv.org/4.x/
