name="Sebatian Sverksmo"
nmbu_email="sebastian.sverkmo@nmbu.no"

name= "Christopher Ljosland Strand"
nmbu_email="christopher.ljosland.strand@nmbu.no"


#task 0
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        print("This animal makes a sound")
    
    
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def make_sound(self):
        print("The dog barks.")
        
class Cat(Animal): 
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def make_sound(self):
        print("The cat meows.")
        
        

Dog = Dog("Dog", 5, "German Shepherd")
Cat = Cat("Cat", 3, "black")

Dog.make_sound()
Cat.make_sound()
    
    
#task 1

class Person: 
    def __init__(self, name, age, email):
        self._name = name
        self._age = age
        self._email = email
    
    def get_details(self): 
        print(f"Name: {self._name} Age: {self._age} Email: {self._email}")


class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self._student_id = student_id
        self._courses = []
        self._grades = {}
        
    def enroll_in_course(self, course):
        self._courses.append(course)
    
    def assign_grade(self, course, grade):
        self._grades[course] = grade
    
    def get_grades(self, ):
        return self._grades
        

class Teacher(Person):
    def __init__(self, name, age, email, subject):
        super().__init__(name, age, email)
        self._subject = subject
    
    def assign_grade(self, student, grade, course): 
        student.assign_grade(grade, course)
        print(f"Grade assigned to {student._name} for {course}: {grade}")
        
        
class Course:
    def __init__(self, course_name, course_code):
        self._course_name = course_name
        self._course_code = course_code
        self._enrolled_students = []
        
    def add_student(self, student): 
        student.enroll_in_course(self._course_code)
        self._enrolled_students.append(student)
        
    def list_students(self): 
        return [student.get_details() for student in self._enrolled_students]
        

Christopher = Student("Christopher", 20, "christopher.ljosland.strand@nmbu.no", "4321")
Sebastian = Student("Sebastian", 25, "sebastian.sverkmo@nmbu.no", "1234")

Jonas = Teacher("Jonas", 30, "jonas.kusch@nmbu.no", "INF201")

INF201 = Course("Videregående programmering" ,"INF201")

INF201.add_student(Christopher)
INF201.add_student(Sebastian)

Jonas.assign_grade(Christopher, "INF201", "A")
Jonas.assign_grade(Sebastian, "INF201", "F")

print("Christopher: ",Christopher.get_grades())
print("Sebastian: ",Sebastian.get_grades())

INF201.list_students()