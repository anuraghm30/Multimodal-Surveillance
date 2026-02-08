import cv2

def record_event(video_source=0, filename="output/event.avi"):
    cap = cv2.VideoCapture(video_source)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480))
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow("Recording", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
