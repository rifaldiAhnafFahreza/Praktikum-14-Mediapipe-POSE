import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Ubah warna ke RGB
    hasil = pose.process(imgRGB)

    if hasil.pose_landmarks:
        mp_draw.draw_landmarks(frame, hasil.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        titik = hasil.pose_landmarks.landmark

        tangan_kanan = titik[mp_pose.PoseLandmark.RIGHT_WRIST.value]
        bahu_kanan = titik[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]

        tangan_kiri = titik[mp_pose.PoseLandmark.LEFT_WRIST.value]
        bahu_kiri = titik[mp_pose.PoseLandmark.LEFT_SHOULDER.value]

        if tangan_kanan.y < bahu_kanan.y:
            cv2.putText(frame, "Tangan Terangkat",
                        (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

        if tangan_kiri.y < bahu_kiri.y:
            cv2.putText(frame, "Tangan Terangkat",
                        (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

    cv2.imshow("Deteksi Angkat Tangan", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
