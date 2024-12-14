# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:52:13 2024

@author: Arumugam
"""
import numpy as np

class SVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None

# [ 2, 3] [ 0, 0 ]
    def fit(self, X, y):
        n_samples, n_features = X.shape
        y_ = np.where(y <= 0, -1, 1)
        
        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                condition = y_[idx] * (np.dot(x_i, self.w) - self.b) >= 1
                if condition:
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    self.w -= self.lr * (2 * self.lambda_param * self.w - np.dot(x_i, y_[idx]))
                    self.b -= self.lr * y_[idx]

    def predict(self, X):
        approx = np.dot(X, self.w) - self.b
        return np.sign(approx)

# Sample data
X = np.array([[1, 2], [2, 3], [3, 3], [2, 1], [3, 2]])
y = np.array([1, 1, -1, -1, -1])
# y_ = np.where(y <= 0, -1, 1)
# Training SVM
svm = SVM()
svm.fit(X, y)
predictions = svm.predict(X)

predictions = svm.predict([100,100])
print("Predictions:", predictions)

# This line of code is used to make predictions by assigning class labels based on the 
# sign of the decision function's output.


y = np.array([1, 0, -1, 2, -2])
y_ = np.where(y <= 0, -1, 1) # 1 <= 0 
# y_ will be: array([1, -1, -1, 1, -1])


# Explanation
# np.sign(x): This function from the NumPy library returns the sign of each element in the array x.
#  It returns:

# 1 for positive numbers
# 0 for zero
# -1 for negative numbers
approx = np.array([2.5, -1.0, 0.0, 4.2, -3.3])

predictions = np.sign(approx)
# # predictions will be: array([ 1., -1.,  0.,  1., -1.])

