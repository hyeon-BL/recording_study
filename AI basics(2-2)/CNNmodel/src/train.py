import numpy as np

class Conv3x3:
    """3x3 Convolution layer using vectorized operations"""

    def __init__(self, num_filters):
        """Initialize filters with random values"""
        self.num_filters = num_filters
        self.filters = np.random.randn(num_filters, 3, 3) / np.sqrt(2 / 9)  # He initialization
    
    
    def forward(self, input): 
        """Vectorized forward pass using im2col"""
        self.last_input = input
        
        # Handle both single images and batches
        if len(input.shape) == 2: # Single image for testing
            h, w = input.shape
        else:
            h, w = input.shape[1], input.shape[2] # Batch of images for training
            
        self.last_input_col = np.lib.stride_tricks.as_strided(
            input,
            shape=(h-2, w-2, 3, 3),
            strides=(input.strides[-2], input.strides[-1], input.strides[-2], input.strides[-1])
        ).reshape(-1, 9)  # Convert to (n_positions, 9) for matrix multiplication
        
        # Reshape filters to (num_filters, 9)
        filters_col = self.filters.reshape(self.num_filters, -1)
        
        # Compute convolution as matrix multiplication
        output = np.dot(self.last_input_col, filters_col.T)
        
        # Reshape output to proper dimensions (h-2, w-2, num_filters)
        return output.reshape(h-2, w-2, self.num_filters)

class MaxPool2:
    def forward(self, input):
        """Vectorized forward pass for max pooling"""
        self.last_input = input
        n_h, n_w, n_c = input.shape
        
        # Reshape input to perform max pooling
        reshaped = input.reshape(n_h//2, 2, n_w//2, 2, n_c)
        self.output = np.max(np.max(reshaped, axis=3), axis=1)
        return self.output


class Softmax:
    """Softmax classifier"""
    def __init__(self, input_len, nodes):
        """Initialize weights and biases"""
        self.weights = np.random.randn(input_len, nodes) / input_len
        self.biases = np.zeros(nodes)

    def forward(self, input):
        """Forward pass"""
        self.last_inshape = input.shape

        input = input.flatten() # Flatten the input 
        self.last_input = input 


        totals = np.dot(input, self.weights) + self.biases # totals = input * weights + biases
        self.last_totals = totals

        exp_a = np.exp(totals)
        return exp_a / np.sum(exp_a, axis = 0) # Apply softmax
    
    def backprop(self, dL_dout, learning_rate):
        """Backpropagation"""
        for i, gradient in enumerate(dL_dout):
            if gradient == 0:
                continue
            
            # Sum of exps to use in backpropagation
            exp_t = np.exp(self.last_totals)
            S = np.sum(exp_t)

            # Gradient of out[i] against totals
            dout_dt = -exp_t[i] * exp_t / (S**2)
            dout_dt[i] = exp_t[i] * (S-exp_t[i]) / (S**2)
            
            # Gradients of totals against weights/biases/input
            dt_dw = self.last_input
            dt_db = 1
            dt_dinputs = self.weights

            # Gradients of loss against totals
            dL_dt = gradient * dout_dt

            # Gradients of loss against weights/biases/input
            dL_dw = dt_dw[np.newaxis].T @ dL_dt[np.newaxis]
            dL_db = dL_dt * dt_db
            dL_dinputs = dt_dinputs @ dL_dt

            # Update weights / biases
            self.weights -= learning_rate * dL_dw
            self.biases -= learning_rate * dL_db
            return dL_dinputs.reshape(self.last_inshape)
        
import struct
import os
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset')
class MNISTDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

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


train_images, train_labels, test_images, test_labels = MNISTDataLoader(data_path).preprocess_data()
test_images = test_images[:1000]
test_labels = test_labels[:1000]

conv = Conv3x3(8)
pool = MaxPool2()
softmax = Softmax(13 * 13 * 8, 10)

def forward(image, label):
    out = conv.forward((image / 255) - 0.5)
    out = pool.forward(out)
    out = softmax.forward(out)

    loss = -np.log(out[label])
    acc = 1 if np.argmax(out) == label else 0

    return out, loss, acc

def train(im, label, lr = .005):
    # Forward
    out, loss, acc = forward(im, label)

    # Calculate initial gradient
    gradient = np.zeros(10)
    gradient[label] = -1/out[label]

    # Backprop
    gradient = softmax.backprop(gradient, lr)

    return loss, acc

def test(images, labels):
    """Evaluate model on test data"""
    loss = 0
    num_correct = 0
    for im, label in zip(images, labels):
        out, l, acc = forward(im, label)
        loss += l
        num_correct += acc
    return loss / len(images), num_correct / len(images) * 100

print("MNIST CNN initialized!")
train_loss = 0
train_correct = 0

for i, (im, label) in enumerate(zip(train_images, train_labels)):
    if i % 100 == 99:
        # Calculate test accuracy
        test_loss, test_accuracy = test(test_images, test_labels)
        print(
            '[Step %d] Past 100 steps: Train Loss %.3f | Train Accuracy: %d%% | Test Loss %.3f | Test Accuracy: %.2f%%' %
            (i + 1, train_loss / 100, train_correct, test_loss, test_accuracy)
        )
        train_loss = 0
        train_correct = 0
    
    l, acc = train(im, label)
    train_loss += l
    train_correct += acc