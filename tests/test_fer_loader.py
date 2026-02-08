from torch.utils.data import DataLoader
from src.dataloaders.fer_loader import FER2013Dataset

# Point to your dataset CSV file
dataset = FER2013Dataset("datasets/FER2013/fer2013.csv")
loader = DataLoader(dataset, batch_size=32, shuffle=True)

# Test: Print the shape of one batch
for x, y in loader:
    print("Batch images shape:", x.shape)   # e.g. torch.Size([32, 3, 224, 224])
    print("Batch labels shape:", y.shape)   # e.g. torch.Size([32])
    break
