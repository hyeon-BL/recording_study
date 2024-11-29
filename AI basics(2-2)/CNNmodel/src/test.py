import numpy as np
import pickle
import os
from data import MNISTDataLoader
from model import CNN

data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset')
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ckpt')

# Load and preprocess data
data_loader = MNISTDataLoader(
    os.path.join(data_path, 'train'),
    os.path.join(data_path, 't10k')
)
_, _, X_test, y_test = data_loader.preprocess_data()

# Initialize network
network = CNN()  # Remove layer_sizes parameter

# Load trained parameters
with open(os.path.join(model_path, 'ckpt.pkl'), 'rb') as f:
    network.parameters = pickle.load(f)