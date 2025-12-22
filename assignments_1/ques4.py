# Write a function to return the sum of digits of number n.

def sum_digits(n):
    sum=0
    for i in range(1, n+1):
        sum+=i

    return sum
    
n=int(input("koi number dalo:"))
print("your answer is:",sum_digits(n))