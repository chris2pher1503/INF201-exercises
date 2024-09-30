name="Sebatian Sverksmo"
nmbu_email="sebastian.sverkmo@nmbu.no"

name= "Christopher Ljosland Strand"
nmbu_email="christopher.ljosland.strand@nmbu.no"

from pathlib import Path
import numpy as np
import time
#cwd is INF201, defined here to make it easier
cwd = Path.cwd()
exercise_4_path = cwd / "Exercises" / "exercise_4"


#task 0:

def create_dir():
    sub_dirs = ["data", "output"]
    projects_task0_path = exercise_4_path / "projects_task0"
    projects_task0_path.mkdir(exist_ok=True)
    for sub_dir in sub_dirs:
        sub_dir_path = projects_task0_path / sub_dir
        if not sub_dir_path.exists():
            sub_dir_path.mkdir()
            file_path = sub_dir_path / (sub_dir + ".txt")
            print(file_path)
            file_path.touch()    
    
    print("task 0 output: ")
    print("-"*60)
    for path in Path.glob(projects_task0_path, "**/*"):
        print(path)
                
        

create_dir()
#task 1:



def create_exercises(total_number=4, project_assigments_start=3):
    exercises = [str(i) if i < project_assigments_start else str(i) + letter for i in range(1, total_number + 1) for letter in (["a", "b"])]
    
    return exercises

def generate_files(exercises):
    students = ["Ole", "Sarah"]

    projects_path  = exercise_4_path / "projects"
    projects_path.mkdir(exist_ok=True)
     
    for exercise in exercises: 
        exercise_path = projects_path / exercise
        exercise_path.mkdir(exist_ok=True)
        
        for student in students:
            student_path = exercise_path / student
            student_path.mkdir(exist_ok=True)

    print("task 1 output: ")
    print("-"*60)
    for path in Path.glob(projects_path, "**/*"):
        print(path)

generate_files(create_exercises())


#task 2: 

def matrix_vector_product(matrix, vector):
    result = [0] * len(matrix) 
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    return result


def numpy_matrix_vector_product(matrix, vector):
    result = np.matmul(matrix, vector)
    
    return result


matrix = [[11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
 [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
 [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
 [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
 [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
 [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
 [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
 [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
 [91, 92, 93, 94, 95, 96, 97, 98, 99, 100],
 [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]]

vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


starttime_non_numpy = time.time()
print(matrix_vector_product(matrix, vector))
endtime_non_numpy = time.time()
starttime_numpy = time.time()
print(numpy_matrix_vector_product(np.array(matrix), np.array(vector)))
endtime_numpy = time.time()
difference_non_numpy = endtime_non_numpy - starttime_non_numpy
difference_numpy = endtime_numpy - starttime_numpy

print(f"Time taken for non-numpy: {difference_non_numpy:.6f}")
print(f"Time taken for numpy: {difference_numpy:.6f}")
print(f"{difference_numpy/difference_non_numpy:.2f} times faster with non numpy")
        