import cv2
import mediapipe as mp

IDX = 1  # en tu Mac suele ser 1
cap = cv2.VideoCapture(IDX, cv2.CAP_AVFOUNDATION)
if not cap.isOpened():
    raise SystemExit("No se pudo abrir la cámara")

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,      # 0 = más rápido, 2 = más preciso
    enable_segmentation=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # mediapipe trabaja en RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = pose.process(rgb)

    if res.pose_landmarks:
        mp_draw.draw_landmarks(
            frame,
            res.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

    cv2.imshow("Pose (ESC para salir)", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
