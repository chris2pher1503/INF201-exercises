name="Sebatian Sverksmo"
nmbu_email="sebastian.sverkmo@nmbu.no"

name= "Christopher Ljosland Strand"
nmbu_email="christopher.ljosland.strand@nmbu.no"

#task 0:
from pathlib import Path
#cwd is INF201, defined here to make it easier
cwd = Path.cwd()
exercise_4_path = cwd / "Exercises" / "exercise_4"


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