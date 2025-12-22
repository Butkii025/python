# practice question

"""given a a list of tuples with info( name:subject).
now derive:
1. list of all unique courses
2. list of student enrolled in maths
3. create dictionary(student, set of courses)

"""

info=[
    ("priya","english"),
    ("anshu","maths"),
    ("priya","maths"),
    ("vijju","hindi"),
    ("vijju","art"),
    ("pv","maths"),
]
print(type(info))
print(info)

for tup in info:
    print(tup[0])  # return name bcz in list name is on 0 index value
    print(tup[1])  # return subject

# 1 all unique courses

unique_courses=set()
for tup in info:
 print(unique_courses.add(tup[1]))

print(unique_courses)

# 2 list student enrolled in maths

for name,course in info:
    if(course=="maths"):
        print(name)

# 3 create dictionary(student, set of courses)

dict={}
for name,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(type(dict))
print(dict)
