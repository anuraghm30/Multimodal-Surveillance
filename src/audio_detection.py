import librosa
import numpy as np
from vggish import VGGish

vggish = VGGish(pretrained=True)

def detect_audio(path):
    y, sr = librosa.load(path, sr=16000)
    mel = librosa.feature.melspectrogram(y=y, sr=sr)
    mel = np.expand_dims(mel, axis=0)
    pred = vggish(mel)
    classes = ["Normal","Scream","Gunshot","GlassBreaking"]
    return classes[np.argmax(pred)]
