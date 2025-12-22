# loops with list

nums=[20,30,90,50,10,40]
x=10
idx=0

for val in nums:
    if (val==x):
        print(f"position of {x} in the list is: {idx}")
        break
    idx+=1


    # btw ☝️ this linear search technique in python
