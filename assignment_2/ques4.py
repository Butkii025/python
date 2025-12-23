""" given a tuple of inegers, create
1. a tuple of all even numbers
2. a tuple of all odd numbers"""

t=[1,2,3,4,5,6,7,8,9]
even_tuple=tuple(x for x in t if x%2==0)
odd_tuple=tuple(x for x in t if x%2!=0)

print("even tuple: ", even_tuple)
print("odd tuple:", odd_tuple)