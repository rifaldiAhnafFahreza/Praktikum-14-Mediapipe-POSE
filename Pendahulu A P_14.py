import cv2
import mediapipe as mp
mpose = mp.solutions.pose #inisiasi media pipe pose
pose = mpose.Pose()
cap = cv2.VideoCapture(0) #video dari webcam

while True:
    success, frame = cap.read() #pembacaan image
    imgrgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #konversi warna
    hasil = pose.process(imgrgb)
    if hasil.pose_landmarks :
        print("terdeteksi")
    else:
        print("tak terdeteksi")


    cv2.imshow('frame',frame)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()