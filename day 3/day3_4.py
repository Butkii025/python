# function in python
def hello():
    print("namaste")

hello()

# example os sum fuction

def sum(a,b):
    sum=a+b
    return sum
print(sum(3,4))
# ans=sum(3,4)
# print(ans)


# let`s take an input for 3 digits and return an average.

def cal_avg( a,b,c):
    sum=a+b+c
    return sum/3
print(cal_avg(3,2,1))

# default value

def sum( a, b=2):
    return a+b
print(sum(3))

#LAMBDA  functions

sum=lambda a,b,c:a+b+c
print(sum(1,2,3))

