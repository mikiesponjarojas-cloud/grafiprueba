# Reporte Técnico: Demo Procedural de Graficación

**Autor:** Miguel Rojas Santillan  
**Materia:** Graficación  
**Entorno:** Python 3, OpenCV, NumPy  

---

## 1. Lista de Escenas y Línea de Tiempo (Timeline)

La demo tiene una duración total de **60 segundos** distribuidos de manera equitativa a una tasa fija de **30 FPS**, generando exactamente 1800 fotogramas. El flujo temporal está automatizado de forma determinista mediante bloques cronometrados de 10 segundos por cada escena, controlados mediante la función de suavizado `smoothstep`.

| Escena | Intervalo de Tiempo | Contenido Visual y Curva Principal | Técnica de Transición Aplicada (Últimos 1.2s) |
| :--- | :--- | :--- | :--- |
| **Escena 1** | 0.0s – 10.0s | Intro, créditos iniciales y **Espiral Logarítmica**. | **Modo 0:** Fundido cruzado de opacidad (*Fade*). |
| **Escena 2** | 10.0s – 20.0s | Animación cíclica de la **Curva de Lissajous**. | **Modo 1:** Destello lumínico (*Flash* blanco armónico). |
| **Escena 3** | 20.0s – 30.0s | **Rosa Polar** con modulación de radio por latidos. | **Modo 2:** Escalado matricial de buffer (*Zoom* lineal). |
| **Escena 4** | 30.0s – 40.0s | **Hipotrocoide** con transformaciones afines geométricas. | **Modo 3:** Cortinilla / Barrido horizontal indexado. |
| **Escena 5** | 40.0s – 50.0s | Campo de **Partículas** con fondo de **Lemniscata**. | **Modo 4:** Cortinilla / Barrido vertical indexado. |
| **Escena 6** | 50.0s – 60.0s | Simulación de **Fuego Procedural** y **Cardioide**. | **Modo 5:** Glitch analógico por canales (*RGB Split*). |

---

## 2. Ecuaciones Matemáticas Utilizadas (Curvas Paramétricas)

El motor gráfico de la demo genera la geometría al vuelo en la CPU traduciendo funciones continuas abstractas a arreglos discretos de píxeles mediante coordenadas paramétricas, mapeadas a variables indexadas en NumPy y dibujadas con `cv2.polylines`. De las 6 curvas implementadas, las 3 principales son:

### A. Curva de Lissajous (Escena 2)
Modula la superposición de dos movimientos armónicos simples en ejes perpendiculares. El desfase dinámico ($\delta$) genera un efecto de oscilación tridimensional aparente.

$$x(\theta) = A \cdot \sin(a \cdot \theta + \delta)$$
$$y(\theta) = B \cdot \sin(b \cdot \theta)$$

*Donde $a$ y $b$ determinan la proporción de frecuencias (moduladas por el tiempo $t$), y $\delta$ representa el desfase angular.*

### B. Rosa Polar (Escena 3)
Genera geometrías armónicas basadas en la frecuencia angular $k$. Para añadir dinamismo procedural, el radio $r$ se multiplica por una función senoidal que emula un pulso o latido rítmico dependiente de $t$.

$$r(\theta) = a \cdot \cos(k \cdot \theta) \cdot (1 + 0.1 \cdot \sin(t \cdot 4))$$
$$x(\theta) = r(\theta) \cdot \cos(\theta + \theta_0)$$
$$y(\theta) = r(\theta) \cdot \sin(\theta + \theta_0)$$

*Donde $k=5$ produce una configuración simétrica de 5 pétalos y $\theta_0$ genera la rotación del plano.*

### C. Hipotrocoide / Spirograph (Escena 4)
Representa la trayectoria trazada por un punto fijo dentro de un círculo de radio $r$ que rueda sobre el interior de una circunferencia mayor de radio $R$.

$$x(\phi) = (R - r) \cos(\phi) + d \cos\left(\frac{R - r}{r} \phi\right)$$
$$y(\phi) = (R - r) \sin(\phi) - d \sin\left(\frac{R - r}{r} \phi\right)$$

*Donde $R=8.0, r=3.0, d=5.0$ dictan la naturaleza estrellada de la curva.*

---

## 3. Transformaciones Implementadas y Composición

Para cumplir con las exigencias del temario sobre manipulación del espacio bidimensional, se implementaron de forma explícita transformaciones geométricas mediante operaciones matriciales:

1. **Transformación Afín $2 \times 3$ (Rotación y Escala Combinadas):** En la **Escena 4**, se calcula dinámicamente una matriz afín de transformación usando el centro geométrico de la pantalla como pivote mediante `cv2.getRotationMatrix2D`. El ángulo se desfasa continuamente en función del tiempo ($t \cdot 45^\circ$) mientras que la escala varía armónicamente. Esta matriz opera sobre las primitivas geométricas y políneas a través de la función de interpolación espacial `cv2.warpAffine`.
2. **Composición Gráfica por Capas:** Para evitar sobreescribir la memoria de video bruscamente, se utiliza composición digital aditiva. La transformación se computa de forma aislada en una matriz o buffer temporal (`layer`). Posteriormente, se realiza una fusión ponderada con el fondo procedural de la escena mediante la ecuación de combinación lineal de canales:
   
   $$\text{Destino} = \alpha \cdot \text{Capa}_1 + \beta \cdot \text{Capa}_2 + \gamma$$
   
   Implementada a nivel de hardware con `cv2.addWeighted` (donde $\alpha=1.0$ y $\beta=1.0$), logrando una superposición limpia sin pérdida de luminancia.

---

## 4. Filtros de Post-Procesado Aplicados (PostFX)

Para elevar el acabado visual del demo y mitigar la dureza matemática de los gráficos vectoriales nativos (evitando que se vea plano o básico), se desarrolló un pipeline secuencial de tres filtros de post-procesado aplicados de forma aditiva sobre el frame final: