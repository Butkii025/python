# #WAP to print a factorial of n.

# n=int(input("enter no: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     print("fact till",i,"is",fact)


# same question with fuction call

def cal_factorial(n):
    fact=1
    for i in range(1, n+1):
        fact=fact*i

    return fact
    
n=int(input("koi number dalo:"))
print("your answer is:",cal_factorial(n))