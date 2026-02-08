import pandas as pd
import numpy as np
import cv2
import torch
from torch.utils.data import Dataset

class FER2013Dataset(Dataset):
    def __init__(self, csv_path, transform=None):
        self.data = pd.read_csv(csv_path)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        pixels = self.data.iloc[idx]["pixels"]
        label = int(self.data.iloc[idx]["emotion"])
        face = np.array(pixels.split(), dtype="uint8").reshape(48,48)
        face = cv2.resize(face, (224,224))
        if self.transform:
            face = self.transform(face)
        return torch.tensor(face).permute(2,0,1).float()/255, label
