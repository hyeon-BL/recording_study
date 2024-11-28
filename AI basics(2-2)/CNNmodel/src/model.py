import numpy as np
import pickle

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


    def backprop(self, d_L_d_out, learn_rate):
        """Vectorized backpropagation"""
        d_L_d_out_reshaped = d_L_d_out.reshape(-1, self.num_filters)  # (n_positions, num_filters)
        
        # Compute gradient w.r.t. filters
        d_L_d_filters = np.dot(d_L_d_out_reshaped.T, self.last_input_col)  # (num_filters, 9)
        d_L_d_filters = d_L_d_filters.reshape(self.num_filters, 3, 3)
        
        # Update filters
        self.filters -= learn_rate * d_L_d_filters
        return None



class MaxPool2:
    """Max pooling layer using vectorized operations"""

    def forward(self, input):
        """Vectorized forward pass for max pooling"""
        self.last_input = input
        n_h, n_w, n_c = input.shape
        
        # Reshape input to perform max pooling
        reshaped = input.reshape(n_h//2, 2, n_w//2, 2, n_c)
        self.output = np.max(np.max(reshaped, axis=3), axis=1)
        return self.output


    def backprop(self, d_L_d_out):
        """Vectorized backpropagation for max pooling"""
        d_L_d_input = np.zeros_like(self.last_input)
        n_h, n_w, n_c = self.last_input.shape
        

        # Create mask of where the maximum values were located
        for c in range(n_c):
            for i in range(0, n_h, 2):
                for j in range(0, n_w, 2):
                    window = self.last_input[i:i+2, j:j+2, c]
                    max_val = np.max(window)
                    mask = (window == max_val)
                    d_L_d_input[i:i+2, j:j+2, c] = mask * d_L_d_out[i//2, j//2, c]
        
        return d_L_d_input



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

class NeuralNetwork:
    """CNN implementation with conv layer, pooling layer, and softmax"""
    def __init__(self):
        # Initialize network architecture
        self.conv = Conv3x3(8)          # Conv layer with 8 filters
        self.pool = MaxPool2()          # Pooling layer
        self.softmax = Softmax(13 * 13 * 8, 10)  # Final classification layer

    def forward(self, image, label):
        """Perform forward pass and return loss and accuracy"""
        # Convert one-hot encoded label to integer
        label_idx = np.argmax(label)
        
        out = self.conv.forward((image / 255) - 0.5)
        out = self.pool.forward(out)
        out = self.softmax.forward(out)

        loss = -np.log(out[label_idx])
        acc = 1 if np.argmax(out) == label_idx else 0

        return out, loss, acc

    def train(self, im, label, lr=.005):
        """Train the network on a single image"""
        # Convert one-hot encoded label to integer
        label_idx = np.argmax(label)
        
        # Forward
        out, loss, acc = self.forward(im, label)

        # Calculate initial gradient
        gradient = np.zeros(10)
        gradient[label_idx] = -1/out[label_idx]

        # Backprop
        gradient = self.softmax.backprop(gradient, lr)
        gradient = self.pool.backprop(gradient)
        self.conv.backprop(gradient, lr)

        return loss, acc

    def compute_loss(self, y_true, y_pred):
        """Calculate cross-entropy loss"""
        y_true = self.to_one_hot(np.argmax(y_true, axis=1) if len(y_true.shape) > 1 else y_true)
        m = y_true.shape[0]
        loss = -np.sum(y_true * np.log(y_pred + 1e-8)) / m
        return loss
    
    def compute_accuracy(self, y_true, y_pred):
        """Calculate prediction accuracy"""
        if len(y_true.shape) == 1:
            y_true = self.to_one_hot(y_true)
        if len(y_pred.shape) == 1:
            y_pred = y_pred.reshape(1, -1)
        return np.mean(np.argmax(y_pred, axis=1) == np.argmax(y_true, axis=1))
    
    def to_one_hot(self, y):
        """Convert integer labels to one-hot encoding"""
        one_hot = np.zeros((y.size, y.max() + 1))
        one_hot[np.arange(y.size), y] = 1
        return one_hot

    def fit(self, X_train, y_train, X_val, y_val, epochs=3, batch_size=64, learning_rate=0.005):
        """Train the network on the given data"""
        n_batches = len(X_train) // batch_size
        
        for epoch in range(epochs):
            print(f'--- Epoch {epoch + 1}/{epochs} ---')
            
            # Shuffle training data
            shuffle = np.random.permutation(len(X_train))
            X_train = X_train[shuffle]
            y_train = y_train[shuffle]
            
            total_loss = 0
            total_acc = 0
            
            # Training
            for i in range(0, len(X_train), batch_size):
                batch_X = X_train[i:i + batch_size]
                batch_y = y_train[i:i + batch_size]
                
                batch_preds = []
                batch_loss = 0
                batch_acc = 0
                
                # Process each sample in the batch
                for im, label in zip(batch_X, batch_y):
                    pred, loss, acc = self.forward(im, label)
                    self.train(im, label, learning_rate)
                    batch_preds.append(pred)
                    batch_loss += loss
                    batch_acc += acc
                
                # Average batch metrics
                batch_loss /= len(batch_X)
                batch_acc /= len(batch_X)
                total_loss += batch_loss
                total_acc += batch_acc
                
                if (i // batch_size) % 100 == 0:
                    print(f'Batch {i//batch_size}/{n_batches}: Loss = {batch_loss:.4f}, Accuracy = {batch_acc:.4f}')
                elif (i // batch_size) == n_batches:
                    print(f'Batch {i//batch_size}/{n_batches}: Loss = {batch_loss:.4f}, Accuracy = {batch_acc:.4f}\n')
            
            # Validation
            print('\n--- Validation ---')
            val_preds = []
            for im, label in zip(X_val, y_val):
                pred, _, _ = self.forward(im, label)
                val_preds.append(pred)
            
            val_preds = np.array(val_preds)
            val_loss = self.compute_loss(y_val, val_preds)
            val_acc = self.compute_accuracy(y_val, val_preds)
            print(f'Validation Loss: {val_loss:.4f}, Accuracy: {val_acc:.4f}\n')
            
        return total_loss/n_batches, total_acc/n_batches
    

    def save_model(self, file_path):
        """Save the model parameters to a file"""
        with open(file_path, 'wb') as f:
            pickle.dump({
                'conv_filters': self.conv.filters,
                'softmax_weights': self.softmax.weights,
                'softmax_biases': self.softmax.biases
            }, f)

    def load_model(self, file_path):
        """Load the model parameters from a file"""
        with open(file_path, 'rb') as f:
            params = pickle.load(f)
            self.conv.filters = params['conv_filters']
            self.softmax.weights = params['softmax_weights']
            self.softmax.biases = params['softmax_biases']