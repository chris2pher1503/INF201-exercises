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
