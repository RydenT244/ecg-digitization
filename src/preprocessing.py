# src/preprocessing.py

import cv2
import numpy as np
from pathlib import Path

def load_image(path):
    img = cv2.imread(str(path))
    return img

if __name__ == "__main__":
    print("Preprocessing module loaded.")

