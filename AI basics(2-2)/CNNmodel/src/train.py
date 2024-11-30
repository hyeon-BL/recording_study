import numpy as np
import os
import pickle
from data import MNISTDataLoader
from model import CNN

# Setup paths
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset')
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ckpt')
os.makedirs(model_path, exist_ok=True)

# Load and preprocess data
data_loader = MNISTDataLoader(data_path)
X_train, y_train, _, _ = data_loader.preprocess_data()

# Split training data into training and validation sets
validation_split = 0.2
split_index = int(len(X_train) * (1 - validation_split))
X_train, X_val = X_train[:split_index], X_train[split_index:]
y_train, y_val = y_train[:split_index], y_train[split_index:]

# Initialize model with learning rate
learning_rate = 0.01  # Can be modified by user
network = CNN(X_train, y_train, X_val, y_val)
num_epochs = 5
batch_size = 500
print(f"Training for {num_epochs} epochs with batch size {batch_size}")

# Training loop
for epoch in range(num_epochs):
    print(f"\nEpoch {epoch+1}/{num_epochs}")
    print("-" * 50)
    total_loss = 0
    indices = np.random.choice(len(X_train), batch_size, replace=False)
    
    for idx, i in enumerate(indices):
        # Forward pass
        X, F1, Z1, A1, F2, Z2, A2, input_1, output_1, activate_1 = network.forward(X_train[i])
        
        # Calculate loss
        loss = network.calculate_loss(activate_1, y_train[i])
        total_loss += loss

        # Backward pass
        costFunc = network.costFunction(activate_1, i)
        network.backpropagate(costFunc, X, F1, Z1, A1, F2, Z2, A2, input_1, output_1, activate_1)

        if (idx + 1) % 100 == 0:
            train_acc, val_acc = network.get_accuracy()
            avg_loss = total_loss / 100
            print(f"Step: {idx+1:4d}/{batch_size}", end=" ")
            print(f"Loss: {avg_loss:.6f}", end=" ")
            print(f"Training Accuracy: {train_acc:.4f}", end=" ")
            print(f"Validation Accuracy: {val_acc:.4f}")
            print("-" * 30)
            total_loss = 0

# Save model
with open(os.path.join(model_path, 'ckpt.pkl'), 'wb') as f:
    pickle.dump(network.parameters, f)

