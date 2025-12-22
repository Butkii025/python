#create a simple calculator that perform arithmetic operations. Creat a function calculatior(a,b, operation) that perform addition, subtraction, multiplication, division, based on the operation parameter.


def calculator(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        if b!=0:
            return a/b
        else:
            return " error, division by Zero"
    else:
        return "invalid operation"

num1=float(input("enter first number: "))
num2=float(input("enter second number: "))
op=input("enter operation(+,-,*,/): ")

result=calculator(num1, num2,op)
print("result is:", result)
