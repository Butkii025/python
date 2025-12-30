# object oriented programming


class Student:
    def __init__(self,name,cgpa):
        self.name= name
        self.cgpa=cgpa

    def get_cgpa(self):
        return self.cgpa



stu1 =Student("priya",8)
stu2 =Student("anshu",9)
stu3 =Student("vijju",7)

print(stu1.name,stu1.cgpa)
print(stu2.name)

print(f"{stu1.name} has get cgpa = {stu1.get_cgpa()}")


