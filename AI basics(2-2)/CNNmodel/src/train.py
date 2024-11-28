import numpy as np
from data import MNISTDataLoader
from model import NeuralNetwork
import os

data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset')
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ckpt/ckpt.pkl')

# Load and preprocess data
data_loader = MNISTDataLoader(
    os.path.join(data_path, 'train'),
    os.path.join(data_path, 't10k')
)
X_train, y_train, _, _ = data_loader.preprocess_data()

# Split training data into training and validation sets
validation_split = 0.2 # 80% training, 20% validation
split_index = int(len(X_train) * (1 - validation_split))
X_train, X_val = X_train[:split_index], X_train[split_index:]
y_train, y_val = y_train[:split_index], y_train[split_index:]


# Initialize the CNN
network = NeuralNetwork()
print("CNN initialized")

# Train the model with specified parameters
epochs = 3
batch_size = 64
learning_rate = 0.001

network.fit(X_train, y_train, X_val, y_val, 
           epochs=epochs, 
           batch_size=batch_size, 
           learning_rate=learning_rate)

# Final test
print('\n--- Final Testing ---')
test_preds = []
for im, label in zip(X_train, y_train):
    pred, _, _ = network.forward(im, label)
    test_preds.append(pred)

test_preds = np.array(test_preds)
final_loss = network.compute_loss(y_train, test_preds)
final_acc = network.compute_accuracy(y_train, test_preds)
print(f'Test Loss: {final_loss:.4f}')
print(f'Test Accuracy: {final_acc:.4f}')


# Save the model
network.save_model(model_path)