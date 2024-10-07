import numpy as np
import random


#task 1: 
matrix = np.random.randint(0, 100, (5000, 5000))

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
A[0][1] = 1
A[0][0] = -2
for i in range(1, len(A)):
    for j in range(1, len(A[i])):
        if i == j:
            A[i][j] = -2
            if j < len(A[i]) - 1:
                A[i][j+1] = 1
            if j < len(A[i]) - 1:
                A[i][j-1] = 1
A[49][48] = 1                
print("A: \n", A)