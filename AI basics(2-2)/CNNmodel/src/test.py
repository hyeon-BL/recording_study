import numpy as np
import pickle
import os
from data import MNISTDataLoader
from model import CNN

data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset')
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ckpt/ckpt.pkl')

# Load and preprocess data
data_loader = MNISTDataLoader(data_path)
X_train, y_train, X_test, y_test = data_loader.preprocess_data()

# Initialize network
network = CNN()  # Remove layer_sizes parameter

# Load trained parameters
with open(model_path, 'rb') as f:
    network.parameters = pickle.load(f)

# Evaluate on test data
test_loss, test_accuracy = network.test(X_test, y_test)
train_loss, train_accuracy = network.test(X_train, y_train)

print("-"*15, "Train results", "-"*15)
print(f"Train Accuracy: {train_accuracy:.2f}%")
print(f"Test Accuracy: {test_accuracy:.2f}%")
print("-"*45)