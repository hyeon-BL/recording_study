import numpy as np
import pickle
import os
from data import MNISTDataLoader
from model import NeuralNetwork

data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset')
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ckpt')

# Load and preprocess data
data_loader = MNISTDataLoader(
    os.path.join(data_path, 'train'),
    os.path.join(data_path, 't10k')
)
_, _, X_test, y_test = data_loader.preprocess_data()

# Initialize network
network = NeuralNetwork()  # Remove layer_sizes parameter

# Load trained parameters
with open(os.path.join(model_path, 'ckpt.pkl'), 'rb') as f:
    network.parameters = pickle.load(f)

# Make predictions
predictions, _ = network.forward(X_test, y_test)

# Calculate accuracy
accuracy = np.mean(np.argmax(predictions, axis=1) == np.argmax(y_test, axis=1))
print(f'Test Accuracy: {accuracy:.4f}')

# Print confusion matrix with validation
pred_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)

# Create confusion matrix to compare predictions
confusion_matrix = np.zeros((10, 10), dtype=int)
for i in range(len(pred_classes)):
    confusion_matrix[true_classes[i]][pred_classes[i]] += 1

print("\nConfusion Matrix:")
print(confusion_matrix)

# Print per-class accuracy
class_accuracy = confusion_matrix.diagonal() / confusion_matrix.sum(axis=1)
for i, acc in enumerate(class_accuracy):
    print(f"Class {i} accuracy: {acc:.4f}")