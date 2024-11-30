import numpy as np
from data import MNISTDataLoader
from model import CNN
import os
        
# Load and preprocess data
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset')
X_train, Y_train, _, _ = MNISTDataLoader(data_path).get_data()
validation_split = 0.2 # 20% of training data for validation
split_idx = int(len(X_train) * (1 - validation_split))
X_train, X_val = X_train[:split_idx], X_train[split_idx:]
Y_train, Y_val = Y_train[:split_idx], Y_train[split_idx:]

# Initialize CNN
cnn = CNN()
epochs = 3
learning_rate = .005
print("\n\n\nCNN initialized!")


# Training loop with epochs
for epoch in range(epochs):
    print(f"\nEpoch {epoch + 1}/{epochs}")
    train_loss = 0
    train_correct = 0
    
    for i, (im, label) in enumerate(zip(X_train, Y_train)):
        if i % 10000 == 9999:
            # Calculate test accuracy
            test_loss, test_accuracy = cnn.test(X_val, Y_val)
            print(
                '[Epoch %d, Step %d] Past 10000 steps: Train Loss %.3f | Train Accuracy: %d%% | Test Loss %.3f | Test Accuracy: %.2f%%' %
                (epoch + 1, i + 1, train_loss / 10000, train_correct / 100, test_loss, test_accuracy)
            )
            train_loss = 0
            train_correct = 0
        
        l, acc = cnn.train(im, label, learning_rate)
        train_loss += l
        train_correct += acc

    # Evaluate on full validation set at the end of each epoch
    test_loss, test_accuracy = cnn.test(X_val, Y_val)
    print(f"\nEpoch {epoch + 1} Complete - Test Accuracy: {test_accuracy:.2f}%")


# Save model after all epochs
save_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ckpt/ckpt.pkl')
cnn.save(save_path)
print(f"Model saved to {save_path}")