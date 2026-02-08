from facenet_pytorch import MTCNN
from efficientnet_pytorch import EfficientNet
import cv2, torch

mtcnn = MTCNN(keep_all=True)
model = EfficientNet.from_pretrained("efficientnet-b0", num_classes=7)  # emotions

def detect_emotion(frame):
    boxes, _ = mtcnn.detect(frame)
    if boxes is not None:
        for box in boxes:
            x1,y1,x2,y2 = map(int, box)
            face = frame[y1:y2, x1:x2]
            face = cv2.resize(face, (224,224))
            face = torch.tensor(face).permute(2,0,1).unsqueeze(0).float()/255
            pred = model(face).argmax().item()
            emotions = ["Angry","Disgust","Fear","Happy","Sad","Surprise","Neutral"]
            return emotions[pred]
    return "No Face"
