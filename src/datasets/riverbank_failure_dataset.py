import torch
from torch.utils.data import Dataset, DataLoader
import rasterio
import numpy as np
from torchvision import transforms
from dotenv import load_dotenv
import os

load_dotenv()

class RiverbankFailureDataset(Dataset):
    def __init__(self, dataset_root, transform=None):
        root = os.getenv('DATASET_ROOT')
        self.file_paths = [os.path.join(root, file) for file in os.listdir(root)]
        self.transform = transform

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, index):
        with rasterio.open(self.file_paths[index], 'r') as infile:
            data = infile.read()  
            if self.transform:
                data = self.transform(data)
        return data