import numpy as np
import struct

class MNISTDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    # Load data from MNIST dataset(ubyte format)
    def load_data(self, tr_label_file, tr_image_file, te_label_file, te_image_file):
        with open(tr_label_file, "rb") as file:
            magic, size = struct.unpack(">II", file.read(8))
            train_labels = np.fromfile(file, dtype=np.dtype(np.uint8).newbyteorder('>'))

        with open(tr_image_file, "rb") as file:
            magic, size = struct.unpack(">II", file.read(8))
            nrows, ncols = struct.unpack(">II", file.read(8))
            data = np.fromfile(file, dtype=np.dtype(np.uint8).newbyteorder('>'))
            train_images = data.reshape((size, nrows, ncols))

        with open(te_label_file, "rb") as file:
            magic, size = struct.unpack(">II", file.read(8))
            test_labels = np.fromfile(file, dtype=np.dtype(np.uint8).newbyteorder('>'))

        with open(te_image_file, "rb") as file:
            magic, size = struct.unpack(">II", file.read(8))
            nrows, ncols = struct.unpack(">II", file.read(8))
            data = np.fromfile(file, dtype=np.dtype(np.uint8).newbyteorder('>'))
            test_images = data.reshape((size, nrows, ncols))

        return train_labels, train_images, test_labels, test_images

    def preprocess_data(self):
        train_labels, train_images, test_labels, test_images = self.load_data(
            f"{self.file_path}/train-labels.idx1-ubyte",
            f"{self.file_path}/train-images.idx3-ubyte",        
            f"{self.file_path}/t10k-labels.idx1-ubyte",
            f"{self.file_path}/t10k-images.idx3-ubyte"
        )

        return train_images, train_labels, test_images, test_labels
