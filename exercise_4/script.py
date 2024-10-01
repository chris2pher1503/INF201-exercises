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
    exercises = [str(i) if i < project_assigments_start else str(i) + letter for i in range(1, total_number + 1) for letter in ["a", "b"]]
    
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


matrix = np.random.rand(5000, 5000)

vector = np.random.rand(5000)


print("task 2 output: ")
print("-"*60)
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
print(f"{difference_non_numpy/difference_numpy:.2f} times faster with numpy")
        