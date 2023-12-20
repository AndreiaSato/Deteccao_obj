import cv2
import numpy as np

# Inicialize a webcam (ou carregue um vídeo)
cap = cv2.VideoCapture(0)  # Use 0 para a webcam padrão ou forneça o nome do arquivo de vídeo

# Inicialize o rastreador (por exemplo, o rastreador de Haar Cascade)
object_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xmln '    

while True:
    # Capture um quadro da webcam (ou do vídeo)
    ret, frame = cap.read()
    if not ret:
        break

    # Converta o quadro para escala de cinza (para detecção de objetos)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecte objetos usando o rastreador (ajuste os parâmetros conforme necessário)
    objects = object_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Desenhe um retângulo ao redor dos objetos detectados
    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Exiba o quadro resultante
    cv2.imshow('Object Tracking', frame)

    # Pressione a tecla 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere a webcam e feche a janela da exibição
cap.release()
cv2.destroyAllWindows()