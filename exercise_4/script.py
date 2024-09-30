name="Sebatian Sverksmo"
nmbu_email="sebastian.sverkmo@nmbu.no"

name= "Christopher Ljosland Strand"
nmbu_email="christopher.ljosland.strand@nmbu.no"

#task 0:





#task 1:
from pathlib import Path


def create_exercises(total_number=4, project_assigments_start=3):
    exercises = [str(i) if i < project_assigments_start else str(i) + letter for i in range(1, total_number + 1) for letter in (["a", "b"])]
    
    return exercises

def generate_files(exercises):
    students = ["Ole", "Sarah"]
    cwd = Path.cwd()
    projects_path  = cwd / "Exercises" / "exercise_4" / "projects"
    projects_path.mkdir(exist_ok=True)
     
    for exercise in exercises: 
        exercise_path = projects_path / exercise
        print(f"Creating exercise directory: {exercise_path}")
        exercise_path.mkdir(exist_ok=True)
        
        for student in students:
            student_path = exercise_path / student
            print(f"Creating student directory: {student_path}")
            student_path.mkdir(exist_ok=True)


generate_files(create_exercises())