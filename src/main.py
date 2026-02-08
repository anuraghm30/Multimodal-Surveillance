from face_emotion import detect_emotion
from pose_detection import detect_pose
from action_detection import detect_action
from audio_detection import detect_audio
from fusion_logic import fusion

import cv2

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    emotion = detect_emotion(frame)
    pose = detect_pose(frame)
    action = "Unknown"   # Placeholder
    audio = "Normal"     # Placeholder

    threat = fusion(emotion, pose, action, audio)
    cv2.putText(frame, f"Threat: {threat}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Surveillance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
