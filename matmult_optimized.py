# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250

def matmult(N):
    # NxN matrix
    X = []
    X = np.random.randint(0, 101, size=(N, N))

    # Nx(N+1) matrix
    Y = []
    Y = np.random.randint(0, 101, size=(N, N+1))
    result = np.dot(X, Y)
    return result
