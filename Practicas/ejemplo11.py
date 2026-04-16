import cv2 
import mediapipe as mp
import math

# Configuración de la nueva Tasks API
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# 1. Crear las opciones del detector
options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=2,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)

# Conexiones de la mano
HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (0, 17), (17, 18), (18, 19), (19, 20)
]

# Captura de video
cap = cv2.VideoCapture(0)
distancia=0

# -------- OBJETOS A MOVER --------
objeto1 = (150,150)
objeto2 = (350,150)
objeto3 = (550,150)
# ---------------------------------

with HandLandmarker.create_from_options(options) as landmarker:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

        results = landmarker.detect(mp_image)

        if results.hand_landmarks:
            for hand_landmarks in results.hand_landmarks:
                h, w, c = frame.shape
                
                keypoints = []
                for landmark in hand_landmarks:
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    keypoints.append((cx, cy))
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

                for connection in HAND_CONNECTIONS:
                    start_idx = connection[0]
                    end_idx = connection[1]
                    cv2.line(frame, keypoints[start_idx], keypoints[end_idx], (0, 255, 0), 2)

                if len(keypoints) >= 9: 
                    x1, y1 = keypoints[4]
                    x2, y2 = keypoints[8]

                    cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.circle(frame, (x1, y1), 8, (0, 0, 255), cv2.FILLED)
                    cv2.circle(frame, (x2, y2), 8, (0, 0, 255), cv2.FILLED)

                    distancia = math.hypot(x2 - x1, y2 - y1)

                    cx_medio, cy_medio = (x1 + x2) // 2, (y1 + y2) // 2

                    cv2.putText(frame, f"{int(distancia)} px", (cx_medio, cy_medio), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                    
                    objeto1 = keypoints[4]   # pulgar
                    objeto2 = keypoints[8]   # índice

                    if len(keypoints) >= 13:
                        objeto3 = keypoints[12]  # medio
                 

        # círculo original del profe
        cv2.circle(frame, (200,200), int(distancia), (21,34,234), -1)

        # 3 OBJETOS 
        cv2.circle(frame, objeto1, 20, (255,0,0), -1)
        cv2.rectangle(frame,(objeto2[0]-20,objeto2[1]-20),(objeto2[0]+20,objeto2[1]+20),(0,255,0),-1)
        cv2.circle(frame, objeto3, 20, (0,0,255), -1)
       

        cv2.imshow("Salida", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()