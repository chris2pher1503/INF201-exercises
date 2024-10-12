name="Sebatian Sverksmo"
nmbu_email="sebastian.sverkmo@nmbu.no"

name= "Christopher Ljosland Strand"
nmbu_email="christopher.ljosland.strand@nmbu.no"

import numpy as np
import random
import time

#task 0:
def inplace_add_vectors(vec1, vec2):
    for i in range(len(vec1)):
        vec1[i] += vec2[i]
    return vec1

def add_vectors(vec1, vec2):
    result = []
    for i in range(len(vec1)):
        result.append(vec1[i] + vec2[i])
    return result

v1 = [1, 2, 3]
v3 = v1.copy()
v2 = [4, 5, 6]

print(inplace_add_vectors(v3, v2))
print(inplace_add_vectors(v1, v2))


#task 1: 
matrix = np.random.randint(0, 101, (5000, 5000))

def sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
    return sum

def mean(matrix, sum):
    mean = sum / (len(matrix) * len(matrix[0]))
    return mean

def variance(matrix, mean):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum += (mean - matrix[i][j]) ** 2
    
    variance =  sum / (len(matrix))**2
    return variance

def multiply(matrix, scalar):
    return matrix * scalar

sum = sum(matrix)
mean = mean(matrix, sum)
variance = variance(matrix, mean)
print("sum of the matrix: ", sum)
print("mean of the matrix: ", mean)
print("variance of the matrix: ",variance)
print("multiplied of the matrix: ",multiply(matrix, 4))
 

#task 2:
A = np.zeros((50 , 50))
print("A: ", A) 

for i in range( len(A)):
    A[i,i] = -2
    if i < (len(A) - 1):
        A[i, i+1] = 1
    if i > 0:
        A[i, i-1] = 1
    
print("A: \n", A)
print("A shape: ", A.shape)


v = np.random.rand(50)
v = v / np.linalg.norm(v)

def dominant_eigenvalue(A, v):
    v_new = np.matmul(A, v)
    v = v_new / np.linalg.norm(v_new)
    return v
    
for i in range(100):
    v = dominant_eigenvalue(A, v)
dominant_eigenvalue = (A @ v) @ v / (v @ v)
print("dominant eigenvalue: ", dominant_eigenvalue)

eigenvalues, eigenvectors = np.linalg.eig(A)
abs_eigenvalues = np.abs(eigenvalues)
dominant_index = np.argmax(abs_eigenvalues)

print("dominant eigenvalue (numpy):", eigenvalues[dominant_index])



