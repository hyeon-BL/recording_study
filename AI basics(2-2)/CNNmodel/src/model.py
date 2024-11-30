import numpy as np


class CNN:
    def __init__(self, tr_x, tr_y, test_x, test_y, learning_rate=0.1):
        """Initialize the CNN model with training and test data"""
        # Training & Test data
        self.tr_x = tr_x
        self.tr_y = tr_y
        self.test_x = test_x
        self.test_y = test_y
        self.learning_rate = learning_rate

        # Weight & Bias 
        self.F1 = np.random.rand(10, 3, 3) / 10
        self.F2 = np.random.rand(10, 10, 3, 3) / 10
        self.W1 = np.random.rand(10, 196) / 10
        self.B1 = np.random.rand(10, 1) / 10
        self.B2 = np.random.rand(10, 1) / 10
        self.B3 = np.random.rand(10, 1) / 10

        # Add parameters property to store trained parameters
        self.parameters = {
            'W1': self.W1,
            'F1': self.F1,
            'F2': self.F2,
            'B1': self.B1,
            'B2': self.B2,
            'B3': self.B3
        }



    def relu(self, input):
        """Relu activation, returns 1-D array of values between [0, inf)"""
        return np.maximum(0.01*input, input)
    
    def softmax(self, input):
        """Softmax activation, returns 1-D array of values between (0, 1]"""
        input = input.T
        for i in range(10):
            input[i] = input[i] - input[i].max()  # Normalize input to prevent overflow
            input[i] = np.exp(input[i]) / np.sum(np.exp(input[i]))
        return input.T
    
    def one_hot(self, index):
        """Converts a single value to one-hot array"""
        one_hot_array = np.zeros((1, np.max(self.tr_y) + 1))
        one_hot_array[np.arange(1), self.tr_y[index]] = 1

        return one_hot_array
    
    def cross_entropy(self, output_layer, index):
        """Cross-entropy loss function for Softmax backpropagation"""
        one_hot_array = self.one_hot(index)
        return (output_layer - one_hot_array)
    
    def costFunction(self, output_layer, index):
        """Cost function using (Softmax - One_hot)"""
        return self.cross_entropy(output_layer, index)
    
    def unpool(self, img, size):
        """Unpooling the image by size"""
        img = img.reshape(-1, 14, 14)
        x = np.repeat(img, size, axis = 2)
        x = np.repeat(x, size, axis = 1)
        return x/.25
    
    def deriv_relu(self, input):
        """Derivative of Relu activation for backpropagation"""
        one_like = np.ones_like(input)  # Create an array of ones with the same shape as x
        one_like[input < 0] = .01
        return one_like
    
  

    
    def im2col(self, filter_len, filter_num, img_size, stride = 1):
        """Transform image into columns for easier matrix multiplication"""

        x_vector = np.tile(np.repeat(np.arange(filter_len) , filter_len), filter_num)
        y_vector = np.tile(np.tile(np.arange(filter_len) , filter_len), filter_num)

        x_vector = np.tile(x_vector, (int((img_size/stride)*(img_size/stride)), 1))
        #Tile y column img_size*img_size times for whole image
        y_vector = np.tile(y_vector, (int((img_size/stride)*(img_size/stride)), 1))

        #Generate increasing numbers by 1 to add onto each of our x and y column
        #(676,)
        every_x_col = np.repeat(np.arange(int(img_size/stride)) * stride, int(img_size/stride)).reshape(-1, 1)
        #(676,)
        every_y_col = np.tile(np.arange(int(img_size/stride)) * stride, int(img_size/stride)).reshape(-1, 1)

        x_vector = x_vector + every_x_col
        y_vector = y_vector + every_y_col

        
        return (x_vector, y_vector)
    
    def col2im(self, input):
        """Outputting N x N error onto gradient"""
        x_pad = np.zeros((10, 30, 30))
        input = input.T.reshape(-1, 10, 9)
        for i in range(28):
            for j in range(28):
                np.add.at(x_pad, (slice(None), np.repeat(np.arange(3), 3)+i, np.tile(np.arange(3), 3)+j), input[(i*28)+j])

        x_pad = x_pad[:, 1:29, 1:29].reshape(-1, 784)/(np.max(np.abs(x_pad)))
        return x_pad

    def clip_gradients(self, gradients, threshold):
        """Gradient Clipping"""
        total = 0

        # Calculate Norm of Gradients
        for grad in gradients:
            total += np.sum(np.square(grad))
        total = np.sqrt(total)
        
        # Clip Gradients with threshold
        if total > threshold:
            for i in range(len(gradients)):
                gradients[i] *= threshold / total

        return gradients


    def forward(self, tr_img):
        """"Forward propagation of weights and bias"""
        # 4 building block (Conv + Relu) -> (Conv + Relu) -> (Conv + Pooling) -> (Softmax)
        
        # Padding from 28x28 to 30x30
        X = tr_img.reshape(784)
        tr_img = np.pad(tr_img, (1, 1), 'constant')
        
        # building block 1. (Conv + Relu)
        x_vector, y_vector = self.im2col(3, 1, 28)
        # (10, 9) * (9, 784) == (10, 784)
        F1 = self.F1.reshape(10, 9)
        cur_img = np.dot(F1, (tr_img[x_vector, y_vector].T)) + self.B1
        Z1 = cur_img
        cur_img = (self.relu(cur_img))
        A1 = cur_img
        cur_img = cur_img.reshape(-1, 28, 28)
        
        # building block 2. (Conv + Relu)
        cur_img = np.pad(cur_img, ((0, 0), (1, 1), (1, 1)), 'constant')
        x_vector, y_vector = self.im2col(3, 1, 28)
        # (10, 10, 9) * (10, 9, 784) -> Im2col -> (10, 90) * (90, 784) == (10, 784)
        # 10 filters is applied on (10 x 28 x 28) images
        F2 = self.F2.reshape(-1, 90)
        cur_img = (np.dot(F2, np.transpose(cur_img[:, x_vector, y_vector], (0, 2, 1)).reshape(90, -1)) + self.B2)
        Z2 = cur_img
        cur_img = (self.relu(cur_img))
        cur_img = cur_img.reshape(-1, 28, 28)
        A2 = cur_img

        # building block 3. (Conv + Pooling)
        x_vector, y_vector = self.im2col(2, 1, 28, 2)
        #(10, 196)
        cur_img = np.sum(cur_img[:, x_vector, y_vector], axis = 2)/4.0


        # building block 4. (Softmax)
        #(10, 196) * (196, 10) = (10, 10)
        input_1 = cur_img
        output_1 = self.W1.dot(input_1.T) + self.B3
        activate_1 = self.softmax(output_1)


        return X, F1, Z1, A1, F2, Z2, A2, input_1, output_1, activate_1

    def calculate_loss(self, output, target_index):
        """Calculate cross-entropy loss"""
        target = self.one_hot(target_index)
        epsilon = 1e-15  # Small constant to avoid log(0)
        output = np.clip(output, epsilon, 1 - epsilon)  # Clip values to avoid numerical instability
        loss = -np.sum(target * np.log(output))
        return loss

    def backpropagate(self, costFunc, X, F1, Z1, A1, F2, Z2, A2, input_1, output_1, activate_1):
        """Backpropagation of weights and bias"""

        # Backpropagation of weights and bias - starting from softmax layer
        #(10, 10) * (10, 196) = (10, 196)
        dW1 = np.dot(costFunc.T, input_1)
        #sum(10, 10) = (10, 1)
        dB3 = np.sum(costFunc.T, axis=1).reshape(10, 1)

        # Backpropagation of weights and bias - starting from pooling layer
        #(10, 10) * (10, 196) = (10, 196)
        dA2 = np.dot(costFunc.T, self.W1)
        dA2 = dA2
        #(10, 196) -> (10, 784)
        dA2 = self.unpool(dA2, 2).reshape(-1, 784)

        # Backpropagation of weights and bias - starting from convolution layer
        #(10, 784) * (10, 784) = (10, 784)
        dZ2 = dA2 * self.deriv_relu(Z2)
        #sum (10, 784) -> (10, 1)
        dB2 = np.sum(dZ2, axis=1).reshape(10, 1)
        #(10, 784) * (784, 10) -> im2col -> (90, 784) * (784, 10) = (90, 10)
        temp_dZ2 = np.pad(dZ2.reshape(-1, 28, 28), ((0, 0), (1, 1), (1, 1)), 'constant')
        x_vector, y_vector = self.im2col(3, 1, 28)
        dF2 = np.dot(np.transpose(temp_dZ2[:, x_vector, y_vector], (0, 2, 1)).reshape(90, -1), A1.T).T


        # Backpropagation of weights and bias - starting from convolution layer
        #(90, 10) * (10, 784) = (90, 784)
        dA1 = F2.T.dot(dZ2)
        dA1 = dA1
        #(90, 784) -> (10, 784) by redistributing the 3x3 convolution
        dA1 = self.col2im(dA1)


        #(10, 784) * (10, 784) = (10, 784)
        dZ1 = dA1 * self.deriv_relu(Z1)
        #sum (10, 784) -> (10, 1)
        dB1 = np.sum(dZ1, axis=1).reshape(10, 1)
        #(10, 784) * (784) -> im2col -> (10, 784) * (784, 9) = (10, 9)
        temp_X = np.pad(X.reshape(28,28), (1, 1), 'constant')
        x_vector, y_vector = self.im2col(3, 1, 28)
        dF1 = dZ1.dot(temp_X[x_vector, y_vector])
        
        #Clipping the Gradient
        dW1, dF1, dF2, dB1, dB2, dB3 = self.clip_gradients([dW1, dF1, dF2, dB1, dB2, dB3], 5)
        lr = self.learning_rate

        self.W1 = np.subtract(self.W1, lr*dW1)
        self.F2 = np.subtract(self.F2, lr*dF2.reshape(-1, 10, 9).reshape(10, -1, 3, 3))
        self.F1 = np.subtract(self.F1, lr*dF1.reshape(10, 9).reshape(-1, 3, 3))

        self.B3 = np.subtract(self.B3, lr*dB3)
        self.B2 = np.subtract(self.B2, lr*dB2)
        self.B1 = np.subtract(self.B1, lr*dB1)

        # Update parameters dictionary after backpropagation
        self.parameters = {
            'W1': self.W1,
            'F1': self.F1,
            'F2': self.F2,
            'B1': self.B1,
            'B2': self.B2,
            'B3': self.B3
        }

        
    def get_accuracy(self): 
        """Calculate Accuracy of predicted labels with true labels"""
        counter_tr = 0
        for i in range(len(self.tr_y)):
            X, F1, Z1, A1, F2, Z2, A2, input_1, output_1, activate_1  = self.forward(self.tr_x[i])
            if np.argmax(np.sum(activate_1, axis=1)) == self.tr_y[i]:
                counter_tr += 1

        counter_te = 0
        for i in range(len(self.test_y)):
            X, F1, Z1, A1, F2, Z2, A2, input_1, output_1, activate_1  = self.forward(self.test_x[i])
            if np.argmax(np.sum(activate_1, axis=1)) == self.test_y[i]:
                counter_te += 1

        return (counter_tr/self.tr_y.size, counter_te/self.test_y.size)


