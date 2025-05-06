import numpy as np
import pickle
class Conv3x3:
    """3x3 Convolution layer using vectorized operations"""

    def __init__(self, num_filters):
        """Initialize filters with random values"""
        self.num_filters = num_filters
        self.filters = np.random.randn(num_filters, 3, 3) / np.sqrt(2 / 9)  # He initialization to prevent vanishing gradients
    
    
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
        totals -= np.max(totals) # Subtract the largest number from totals to prevent overflow
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
        
class CNN:
    def __init__(self):
        """Buiding block(convolution, pooling, softmax)"""
        self.conv = Conv3x3(8)
        self.pool = MaxPool2()
        self.softmax = Softmax(13 * 13 * 8, 10)

    @property
    def parameters(self):
        """Get model parameters for saving"""
        return {
            'conv_filters': self.conv.filters,
            'softmax_weights': self.softmax.weights,
            'softmax_biases': self.softmax.biases
        }
    
    @parameters.setter
    def parameters(self, params):
        """Restore model parameters from saved state"""
        self.conv.filters = params['conv_filters']
        self.softmax.weights = params['softmax_weights']
        self.softmax.biases = params['softmax_biases']

    def forward(self, image, label):
        """Forward pass"""
        out = self.conv.forward((image / 255) - 0.5) # Normalize pixel values to [-0.5, 0.5]
        out = self.pool.forward(out)
        out = self.softmax.forward(out)

        loss = -np.log(out[label]) # Cross-entropy loss
        acc = 1 if np.argmax(out) == label else 0

        return out, loss, acc

    def train(self, im, label, lr):
        """Train the model"""
        # Forward pass
        out, loss, acc = self.forward(im, label)

        # Calculate initial gradient
        gradient = np.zeros(10)
        gradient[label] = -1/out[label] # Derivative of cross-entropy loss written in terms of softmax output

        # Backpropagate gradient
        gradient = self.softmax.backprop(gradient, lr)
        gradient = self.pool.backprop(gradient)
        self.conv.backprop(gradient, lr)
        
        # Clip the gradient to prevent exploding gradients
        np.clip(gradient, -1, 1, out=gradient)

        return loss, acc

    def test(self, images, labels):
        """Evaluate model on test data"""
        loss = 0
        num_correct = 0
        for im, label in zip(images, labels):
            out, l, acc = self.forward(im, label)
            loss += l
            num_correct += acc
        return loss / len(images), num_correct / len(images) * 100 # Return loss and accuracy
    
    def save(self, path):
        """Save model parameters"""
        with open(path, 'wb') as f:
            pickle.dump(self.parameters, f)