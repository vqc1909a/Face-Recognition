import cv2

cap = cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

count = 60

while (cap.isOpened()):
   ret, frame = cap.read()

   frame = cv2.resize(frame, (1366, 768))
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   scaleFactor = 1.25
   minNeighbors = 5

   faces = faceClassif.detectMultiScale(gray, scaleFactor, minNeighbors)
   
   for (x, y, w, h) in faces:
       cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)

   cant_faces = len(faces)
   aforo = 5

   cv2.putText(frame, f'Numero de caras detectadas: {cant_faces}', (
       825, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 239), 5, cv2.FILLED)

   cv2.putText(frame, f'AFORO: {aforo}', (825, 100),
               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 239), 5, cv2.FILLED)

   cv2.putText(frame, "Salir de la aplicacion: Tecla s", (825, 150),
               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.FILLED)

   if cant_faces > aforo:
      count = count - 1
      cv2.putText(frame, f'AFORO SOBREPASADO', (50, 225),
                  cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5, cv2.FONT_HERSHEY_SIMPLEX)
      cv2.putText(frame, f'CERRANDO APLICACION EN: {count} segundos', (
          50, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5, cv2.FONT_HERSHEY_SIMPLEX)
   else:
      count = 60

   if count == 0:
      break

   cv2.imshow('frame', frame)

   if cv2.waitKey(1) & 0xFF == ord('s'):
      break

cap.release()
cv2.destroyAllWindows()
