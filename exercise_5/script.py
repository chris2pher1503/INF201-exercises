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

print("sum of the matrix: ", sum(matrix))
print("mean of the matrix: ", mean(matrix, sum(matrix)))
print("variance of the matrix: ",variance(matrix, mean(matrix, sum(matrix))))
print("multiplied of the matrix: ",multiply(matrix, 4))






""" def mean(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])): 
            sum += int(matrix[i][j])
    mean_value = sum / (len(matrix) * len(matrix[0]))
                       
    return mean_value

def variance(matrix, mean):
    sum= 0
    for i in range (len(matrix)):
        for j in range(len(matrix[i])):
            sum += (mean - matrix[i][j]) ** 2
    return sum / (len(matrix) * len(matrix[0]))**2 """



""" def multiplt(matrix, scalar):
    return matrix * scalar


print(mean(matrix))
print(variance(matrix))
print(sum(matrix))
print(multiplt(matrix, 4))

 """
 
 #task 2: 
 