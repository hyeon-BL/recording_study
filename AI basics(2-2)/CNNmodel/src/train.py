import numpy as np
from data import MNISTDataLoader
from model import CNN
import os
        

data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset')
train_images, train_labels, test_images, test_labels = MNISTDataLoader(data_path).preprocess_data()
test_images = test_images[:1000]
test_labels = test_labels[:1000]

cnn = CNN()
epochs = 3
learning_rate = .005


print("MNIST CNN initialized!")
train_loss = 0
train_correct = 0

for i, (im, label) in enumerate(zip(train_images, train_labels)):
    if i % 100 == 99:
        # Calculate test accuracy
        test_loss, test_accuracy = cnn.test(test_images, test_labels)
        print(
            '[Step %d] Past 100 steps: Train Loss %.3f | Train Accuracy: %d%% | Test Loss %.3f | Test Accuracy: %.2f%%' %
            (i + 1, train_loss / 100, train_correct, test_loss, test_accuracy)
        )
        train_loss = 0
        train_correct = 0
    
    l, acc = cnn.train(im, label, learning_rate)
    train_loss += l
    train_correct += acc