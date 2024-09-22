import torch
import rasterio
import numpy as np
from torchvision import transforms
from dotenv import load_dotenv
import os

from torchvision.datasets import ImageFolder

load_dotenv()


class RiverbankFailureDataset(ImageFolder):
    def __init__(self, dataset_root, root: str, transform=None):
        super().__init__(root, transform)
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
