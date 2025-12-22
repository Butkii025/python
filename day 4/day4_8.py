#sets ::: only store unique elements

set={1,2,2,2,3,4,5,6}
set2={5,6,8,9}
print(type(set))
print(set)  
print(len(set))

# methods

print(set.add(7))
print(set.remove(3))


print(set.union(set2))
print(set.intersection(set2))