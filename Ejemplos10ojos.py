import cv2 as cv 

rostro = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv.VideoCapture(0)

while True:
    ret, img = cap.read()
    gris = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gris, 1.3, 5)

    for(x,y,w,h) in rostros:
        res = int((w+h)/8)

        img = cv.rectangle(img, (x,y), (x+w, y+h), (234, 23,23), 5)

        # Ojos
        img = cv.circle(img, (x + int(w*0.3), y + int(h*0.4)) , 21, (0, 0, 0), 2 )
        img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) , 21, (0, 0, 0), 2 )
        img = cv.circle(img, (x + int(w*0.3), y + int(h*0.4)) , 20, (255, 255, 255), -1 )
        img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) , 20, (255, 255, 255), -1 )
        img = cv.circle(img, (x + int(w*0.3), y + int(h*0.4)) , 5, (0, 0, 255), -1 )
        img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) , 5, (0, 0, 255), -1 )
        # Oreja izquierda
        img = cv.circle(img, (x - int(w*0.1), y + int(h*0.35)), int(w*0.12), (255, 220, 200), -1)
        img = cv.circle(img, (x - int(w*0.1), y + int(h*0.35)), int(w*0.07), (255, 180, 180), -1)

        # Oreja derecha
        img = cv.circle(img, (x + w + int(w*0.1), y + int(h*0.35)), int(w*0.12), (255, 220, 200), -1)
        img = cv.circle(img, (x + w + int(w*0.1), y + int(h*0.35)), int(w*0.07), (255, 180, 180), -1)
        # Nariz
        img = cv.circle(img, (x + int(w*0.5), y + int(h*0.55)), 10, (0,0,0), -1)
        
        #Orejas
        


        # Boca
        img = cv.ellipse(img,
                         (x + int(w*0.5), y + int(h*0.75)),  # centro
                         (int(w*0.2), int(h*0.08)),          # tamaño
                         0, 0, 180,                          # forma sonrisa
                         (0,0,255), 3)

        img = cv.rectangle(img, (x+10,y+10), (x+w, y+h), (234,0 ,234), 5)

        img2=  img[y:y+h,x:x+w]
        cv.imshow('img2', img2)

    cv.imshow('img', img)

    if cv.waitKey(1)== ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()