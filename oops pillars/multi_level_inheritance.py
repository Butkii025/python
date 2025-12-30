# mutli level inheritance

class Employee:
    start_time="10am"
    end_time="6pm"

class Admin(Employee):    # level one
    def __init__(self, role):
        self.role = role

class Accountant(Admin):    # level two
    def __init__(self, salary,role):
        super().__init__(role)
        self.salary = salary

acc1= Accountant(20000, "engineer")
print(f"His role is {acc1.role} with salary {acc1.salary} and his timing is {acc1.start_time} to {acc1.end_time} .")



