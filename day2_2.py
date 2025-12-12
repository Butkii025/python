# type conversion

a=5
b=3.14
print(type(a))
sum=a+b
print(sum)
print("sum of number is :",sum, type(sum))

#float priority is more than integer here, that`s why it reflecting th float

# type casting

x=2.3 # it`s a float value
x=int(x) # here it chnages to boolean
print(type (x))

y=5
add=x+y
print(add, type(add)) # type would be int bcz, we changed (2.3) into int type, so ans is 7 instead of 7.3
