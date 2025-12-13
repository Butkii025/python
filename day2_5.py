# conditional statements

age=int(input("enter your age: "))
if age>=18:
    print(" you can vote ")
else:
    print("you can`t vote buddy")
    

# second traffic light

color= input("enter color: ")

if color=="red":
    print("stop")
elif color=="yellow":
    print("ready to go buddy")
elif color=="green":
    print("go")
else: print("wrong color input")

# check no, is multiple of 5 or not

A=int(input("enter you number: "))
if (A%5==0):
    print(" it`s a multiple of 5.")
else:
    print(" not a multiple of 5.")

# check if the number is even or odd

if(A%2==0):
    print("it`s a even number")
else:
    ("it`s a odd number")
   
# nesting ( codition under condition)

username=input(" enter your username: ")
password=input("enter your password: ")
if (username=="admin" and password=="pass"):
    print("LOGIN succesfully !")
else:
    if(username!="admin"):
        print("wrong username")
    else:
        print("wrong password")

# WAP to prin the pattern
print('x\t y\t x**y')
print("10\t2\t", 10**2)
print("20\t4\t", 20**4)
print("30\t6\t", 30**6)
