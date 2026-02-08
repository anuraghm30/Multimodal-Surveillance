# Simplified pipeline – assumes you have pretrained TimeSformer
import torch
from timesformer.models.vit import TimeSformer

model = TimeSformer(img_size=224, num_classes=400, num_frames=8,
                    attention_type='divided_space_time', pretrained_model='timesformer.pth')

def detect_action(frames):  # frames = list of 8 consecutive frames
    inputs = torch.tensor(frames).unsqueeze(0).float()
    pred = model(inputs)
    return torch.argmax(pred).item()
