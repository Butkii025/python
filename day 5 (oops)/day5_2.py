# attributes
# there are two type:  class  && instance

class student:
    college_name="DSMNRU"  # class attribute
    def __init__(self, name, cgpa):
        self.name = name  # instance attribute
        self.cgpa= cgpa

stu1 = student("Rahul", 8.9)
print(stu1.name)
print(student.college_name)