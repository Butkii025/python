# question no.3: WAP of function to print the digits of a number, and length in numbers
def count_digits(n):
    if n==0:
        return 1
    count=0
    n= abs(n)

    while n>0:
     count+=1
     n//=10
    return count

num=int(input("enter a number: "))
print(" number if digit:", count_digits(num))

