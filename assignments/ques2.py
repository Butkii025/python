# question no.2: write a fuction that takes two inetegers A and B and print all even no. b/w them


def cal_even( a, b):
    for num in range(a, b+1):
        if num%2==0:
            print(num)
a=int(input("enter first number: "))
b=int(input("enter second number: "))

cal_even(a,b)