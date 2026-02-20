# ## Proyecto 4:

# ## En este proyecto, vamos a crear una aplicación que utiliza la webcam para detectar las manos utilizando la biblioteca OpenCV y el módulo de detección de manos de cvzone. 
# # La aplicación mostrará la imagen de la webcam con las manos detectadas y sus coordenadas.


# import cv2
# ## Me permite importar la clase HandDetector del módulo HandTrackingModule de la biblioteca cvzone
# from cvzone.HandTrackingModule import HandDetector

# ## Función para detectar la cámara disponible
# import time
# ## Esta función intenta abrir las cámaras disponibles 
# # y devuelve el índice de la primera cámara que se puede abrir correctamente.  
# def pick_camera(max_idx=3):
#     for i in range(max_idx):
#         cap = cv2.VideoCapture(i, cv2.CAP_AVFOUNDATION)
#         if not cap.isOpened():
#             cap.release()
#             continue
#         time.sleep(0.2)
#         ret, frame = cap.read()
#         mean = float(frame.mean()) if ret and frame is not None else 0.0
#         cap.release()
#         if mean > 1.0:
#             return i
#     return 0

# IDX = pick_camera()
# cap = cv2.VideoCapture(IDX, cv2.CAP_AVFOUNDATION)
# print("Usando cámara IDX =", IDX)


# ## Me permite abrir la webcam
# webcam = cv2.VideoCapture(1)

# ## Me permite verificar si la webcam se abrió correctamente
# if not cap.isOpened():
#     raise RuntimeError("No se pudo abrir la cámara. Probá IDX=0 o IDX=1.")


# ## Me permite crear un objeto de la clase HandDetector con una confianza de 
# # detección del 80% y un máximo de 2 manos detectadas
# rastreador = HandDetector(detectionCon=0.8, maxHands=2)

# ## El ciclo while se ejecutará de forma indefinida
# while True:

#     ## Me permite leer la imagen de la webcam y nos entrega 2 valores 
#     exito, imagen = webcam.read()

#     ## Me permite redimensionar la imagen a un tamaño de 1280x720 píxeles
#     imagen = cv2.resize(imagen, (1280, 720))

#     ## Me permite detectar las manos en la imagen de la webcam,
#     ## y nos da imagen de las manos y coordenadas de las manos
#     coordenadas, imagen_manos = rastreador.findHands(imagen)

#     print(coordenadas)

#     ## Me permite mostrar la imagen de la webcam
#     cv2.imshow("Proyecto 4 - IA", imagen)

#     ## Me permite salir del ciclo while al presionar cualquier tecla
#     if cv2.waitKey(1) != -1:
#         break

# ## Me permite liberar la webcam y cerrar las ventanas
# webcam.release()
# ## Me permite cerrar las ventanas
# cv2.destroyAllWindows()

## Proyecto 4: Webcam con OpenCV


import cv2
## Me permite importar la clase HandDetector del módulo HandTrackingModule de la biblioteca cvzone
from cvzone.HandTrackingModule import HandDetector
import time

## Función para detectar la cámara disponible
def pick_camera(max_idx=3):
    for i in range(max_idx):
        cap = cv2.VideoCapture(i, cv2.CAP_AVFOUNDATION)
        if not cap.isOpened():
            cap.release()
            continue
        time.sleep(0.2)
        ret, frame = cap.read()
        mean = float(frame.mean()) if ret and frame is not None else 0.0
        cap.release()
        if mean > 5.0:
            return i
    return 0
## Me permite detectar la cámara disponible y obtener su índice
IDX = 1
webcam = cv2.VideoCapture(IDX, cv2.CAP_AVFOUNDATION)
print("Usando cámara IDX =", IDX)
## Me permite verificar si la webcam se abrió correctamente
if not webcam.isOpened():
    raise RuntimeError("No se pudo abrir la cámara.")
## Me permite crear un objeto de la clase HandDetector con una confianza de 
# detección del 80% y un máximo de 2 manos detectadas   
rastreador = HandDetector(detectionCon=0.8, maxHands=2)
## El ciclo while se ejecutará de forma indefinida
while True:
    exito, imagen = webcam.read()
    ## Me permite verificar si se pudo leer el frame de la cámara correctamente
    if not exito or imagen is None:
        print("No pude leer frame de la cámara")
        continue
## Me permite redimensionar la imagen a un tamaño de 1280x720 píxeles
    imagen = cv2.resize(imagen, (1280, 720))
## Me permite detectar las manos en la imagen de la webcam,
    coordenadas, imagen_manos = rastreador.findHands(imagen)
    print(coordenadas)
## Me permite mostrar la imagen de la webcam
    cv2.imshow("Proyecto 4 - IA", imagen)

    # ESC para salir (mejor que 'cualquier tecla' porque a veces detecta teclas raras)
    if cv2.waitKey(1) & 0xFF == 27:
        break
## Me permite liberar la webcam y cerrar las ventanas
webcam.release()
## Me permite cerrar las ventanas
cv2.destroyAllWindows()

