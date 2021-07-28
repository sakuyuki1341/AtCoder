import numpy as np
from numpy import linalg as LA

A = np.array([[3, 1],[1, 1]])

print(LA.cond(A, 2))