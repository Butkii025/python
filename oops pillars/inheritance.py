# inheritance

# single level inheritance

class Employee:
    start_time="10am"
    end_time="6pm"

class Teacher(Employee):
    def __init__(self,subject):
        self.subjet = subject

t1= Teacher("maths")

print(f"t1 have {t1.subjet} as subject with start time {t1.start_time} and end time {t1.end_time} .")

# print(t1.subjet, t1.start_time, t1.end_time)




