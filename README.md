# 🖼️ Segmentación de Bordes en Imágenes usando Canny

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5.0+-green.svg)](https://opencv.org/)
[![Managed with uv](https://img.shields.io/badge/managed_with-uv-purple.svg)](https://github.com/astral-sh/uv)

Una aplicación sencilla, pero poderosa, para la detección y segmentación de bordes en imágenes utilizando el clásico **Algoritmo de Canny** mediante la librería OpenCV en Python.

Este proyecto forma parte de estudios y prácticas en el campo de **Visión Computacional**.

## 📌 Características

- **Carga de imágenes estáticas:** Lee directamente formatos estándar de imagen.
- **Pre-procesamiento automatizado:** Conversión instantánea a escala de grises para un análisis morfológico óptimo.
- **Detección de bordes precisa:** Extrae líneas y contornos utilizando el eficiente detector Canny.
- **Interfaz de visualización:** Comparación sencilla lado a lado entre la imagen original y el resultado procesado.

## 🛠️ Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu sistema para poder ejecutar este entorno:
- [Python 3.13](https://www.python.org/) o superior.
- [uv](https://docs.astral.sh/uv/) (El manejador de dependencias y entornos utilizado en este proyecto).

## 🚀 Instalación y Configuración

Sigue estos pasos para levantar el proyecto en tu entorno local siguiendo las mejores prácticas:

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/elisbanpaco/segmentacion-imagen-canny.git
   cd segmentacion-imagen-canny
   ```

2. **Sincroniza y crea el entorno virtual:**
   Dado que este proyecto usa `uv` para su gestión, basta con ejecutar:
   ```bash
   uv sync
   ```
   *Esto leerá el archivo `pyproject.toml` y el `uv.lock`, instalando las versiones exactas de las dependencias (`opencv-python`) de manera ultra-rápida dentro de un entorno virtual `.venv` aislado.*

3. **Activa el entorno virtual:**
   - En sistemas basados en Unix (Linux/macOS):
     ```bash
     source .venv/bin/activate
     ```
   - En Windows:
     ```bash
     .venv\Scripts\activate
     ```

## 🎮 Uso

Para ejecutar el detector de bordes, asegúrate de tener una imagen válida y corre el script principal:

```bash
python app.py
```

> 💡 **Tip:** Por defecto, el script busca una imagen de prueba en la ruta `imgs/perrito.jpeg`. Si deseas analizar tu propia imagen, colócala en el directorio `imgs/` y actualiza la ruta cargada en `cv2.imread()` dentro del archivo `app.py`.

Al ejecutarse, la aplicación abrirá dos ventanas:
1. La imagen a color original.
2. La imagen con los bordes detectados.

Para cerrar las ventanas y terminar la ejecución del programa de forma segura, simplemente **presiona cualquier tecla** mientras estás en la ventana de OpenCV.

## 🧠 Entendiendo el Código (Para la Comunidad)

El script base (`app.py`) utiliza `cv2.Canny()` de OpenCV, cuyo poder reside en la afinación de sus umbrales (Hysteresis Thresholding):

```python
edges = cv2.Canny(gray_image, 20, 50)
```

- **Imagen en Grises (`gray_image`):** La base sobre la cual el algoritmo detecta gradientes (cambios de intensidad lumínica).
- **Umbral Inferior (`20`):** Límite mínimo de intensidad del gradiente. Los píxeles con un valor por debajo de este umbral se descartan por completo (no son bordes).
- **Umbral Superior (`50`):** Límite máximo. Los píxeles con un gradiente que supera este número son clasificados automáticamente como *bordes fuertes*.

Los gradientes que caen entre **20 y 50** solo serán considerados bordes si están físicamente conectados a un píxel que sea clasificado como borde fuerte. ¡Te invitamos a modificar estos valores en el código para experimentar cómo cambia la sensibilidad de detección!

## 🤝 Contribuciones

¡Las contribuciones de la comunidad son clave para crecer! Si deseas mejorar el proyecto, documentarlo mejor, o añadir características (como ajuste en tiempo real con *trackbars*):

1. Haz un *Fork* del proyecto.
2. Crea una rama para tu feature (`git checkout -b feature/MejoraIncreible`).
3. Haz un *Commit* de tus cambios (`git commit -m 'Añadir MejoraIncreible'`).
4. Sube la rama (`git push origin feature/MejoraIncreible`).
5. Abre un *Pull Request* para que lo revisemos.

---
*Hecho con dedicación para la comunidad de entusiastas en Visión Computacional.*
