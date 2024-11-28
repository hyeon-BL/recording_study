import numpy as np
import struct

class MNISTDataLoader:
    def __init__(self, train_path, test_path):
        self.train_labels = self.load_labels(f"{train_path}-labels.idx1-ubyte")
        self.train_images = self.load_images(f"{train_path}-images.idx3-ubyte")
        self.test_labels = self.load_labels(f"{test_path}-labels.idx1-ubyte")
        self.test_images = self.load_images(f"{test_path}-images.idx3-ubyte")
    
    def load_labels(self, filepath):
        with open(filepath, 'rb') as f:
            magic, num = struct.unpack(">II", f.read(8))
            labels = np.fromfile(f, dtype=np.uint8)
        return labels
    
    def load_images(self, filepath):
        with open(filepath, 'rb') as f:
            magic, num, rows, cols = struct.unpack(">IIII", f.read(16))
            images = np.fromfile(f, dtype=np.uint8).reshape(num, rows, cols)
        return images

    def to_one_hot(self, labels):
        """Convert labels to one-hot encoding"""
        one_hot = np.zeros((labels.size, 10))
        one_hot[np.arange(labels.size), labels] = 1
        return one_hot
       
    def preprocess_data(self):
        # Process features and labels
        X_train = self.train_images  # Shape: (60000, 28, 28)
        y_train = self.to_one_hot(self.train_labels)  # Shape: (60000, 10)
        X_test = self.test_images    # Shape: (10000, 28, 28)
        y_test = self.to_one_hot(self.test_labels)    # Shape: (10000, 10)
        
        # Normalize pixel values to [0, 1]
        X_train = X_train / 255.0
        X_test = X_test / 255.0
        
        return X_train, y_train, X_test, y_test

    # Remove or comment out _to_one_hot method as it's no longer needed