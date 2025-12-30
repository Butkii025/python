# multiple inheritance

class Teacher:
    def __init__(self, salary):
        self.salary= salary

class Student:    # level one
    def __init__(self, cgpa):
        self.cgpa= cgpa

class TA(Teacher, Student):
    def __init__(self, salary, cgpa, name):
        super().__init__(salary)
        Student.__init__(self, cgpa)
        self.name=name

ta1= TA(15000, 9.3, "vijjy")
print(ta1.name, ta1.cgpa, ta1.salary)



