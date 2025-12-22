# tuples in python

tup=[1,2,2,3,4,5,2,6]
print(tup[2])
sum=0
for val in tup:
    sum+=val

print(f"sum of tup is: {sum}")

# slicing methods in tuple is same as list

#tuple methods

print(tup.index(2))
print(tup.count(2))
