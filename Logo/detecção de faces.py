import cv2
imagem = cv2.imread('pessoas.jpg')
classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = classificador.detectMultiScale(imagemcinza, scaleFactor=1.09,
                                           minNeighbors=5,
                                           minSize=(30,30),
                                           maxSize=(40,40))

print(deteccoes)
print(len(deteccoes))

for (x, y, l, a) in deteccoes:
    cv2.rectangle(imagem, (x,y), (x+l,y+a), (0,255,0), 2)

cv2.imshow('Detector de Faces', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
