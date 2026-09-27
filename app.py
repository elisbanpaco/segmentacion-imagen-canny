# Aplicacion de imagenes segmentadas por bordes usando canny

import cv2

# Cargar la imagen
image = cv2.imread('imgs/perrito.jpeg')

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # tambine puedes cambiar a cv2.COLOR_BGR2RGB para cambiar el color de la imagen

# Aplicar el detector de bordes Canny
edges = cv2.Canny(
    gray_image, # Imagen en escala de grises
    20,        # Valor umbral inferior , es el valor que se utiliza para identificar los bordes más débiles en la imagen. Los píxeles con un gradiente de intensidad por debajo de este valor se consideran no bordes y se descartan. 
    50         # Valor umbral superior , es el valor que se utiliza para identificar los bordes más fuertes en la imagen. Los píxeles con un gradiente de intensidad por encima de este valor se consideran bordes y se incluyen en el resultado final.
    )

# Mostrar la imagen original y la imagen con bordes detectados
cv2.imshow('Imagen Original', image)
cv2.imshow('Bordes Detectados', edges)

# Esperar a que se presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

