# write a function is_prime(n) that return True if n is Prime and False otherwise.


def is_prime(n):
 if n<=1:
  return False
 i = 2
 while i*i <= n:
   if n % i == 0:
    return False
   i+=1
 return True
    
num=int(input("enter a number: "))
print(f"num: {num}", is_prime(num))
