# matrix multiplication 
# https://www.digitalocean.com/community/tutorials/numpy-matrix-multiplication

import numpy as np

A = np.array([[1, -1],
              [7, 4]])
B = np.array([[-3, 2],
              [5, 9]])

C = np.multiply(A, B)

print(C)
