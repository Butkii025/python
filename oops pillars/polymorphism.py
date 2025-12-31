# polymorphism : is a multiple function with same name having similar work
# overloading, overriding, overwritting

class Employee:
    def get_designation(self):
        print(" designation= Employee")

class Teacher(Employee):     # here uses the same class and create an case of (override) 
     def get_designation(self):
        print(" designation= Teacher")   # hence the designation will printed as Teacher instead of Employee

t1= Teacher()
t1.get_designation()
