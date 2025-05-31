import cv2
import random  # Importar la librería random
import tensorflow as tf
import numpy as np

modelo = tf.keras.models.load_model("numbers.h5")

# Abrir la cámara
cap = cv2.VideoCapture(1)

# Verificar si la cámara está abierta
if not cap.isOpened():
    print("Error: No se puede acceder a la cámara.")
    exit()

while True:
    # Capturar el frame
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo leer el frame.")
        break
    
    # Obtener el tamaño de la imagen (alto y ancho)
    height, width = frame.shape[:2]
    
    # Calcular el tamaño de la RoI (1/3 del tamaño de la imagen)
    roi_size = int(min(height, width) / 1.75)
    
    # Calcular las coordenadas de la RoI para que esté centrada
    x_start = (width - roi_size) // 2
    y_start = (height - roi_size) // 2
    
    # Definir la RoI
    roi = frame[y_start:y_start+roi_size, x_start:x_start+roi_size]
    
    # Convertir la RoI a escala de grises (un solo canal)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    # Aplicar un filtro gaussiano a la RoI
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Umbralizar la RoI
    _, thresholded = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
    
    inv = 255.0 - thresholded

    redim = cv2.resize(inv, (28, 28))

    norm = redim / 255.0

    entrada = np.expand_dims(norm, axis=(0, -1))

    prediccion = modelo.predict(entrada)
    
    # Escribir el valor aleatorio en el frame
    cv2.putText(frame, f"Valor: {np.argmax(prediccion)}", (250, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

    # Mostrar el frame con la RoI resaltada
    cv2.rectangle(frame, (x_start, y_start), (x_start + roi_size, y_start + roi_size), (255, 0, 0), 3)
    
    # Mostrar la imagen original y procesada
    cv2.imshow("Frame", frame)
    cv2.imshow("Thresholded RoI", thresholded)
    
    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()



