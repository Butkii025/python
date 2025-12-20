# design a program to continously input a number n from user & print if it is positive or negative until user print "Quit" .

while True:
 n=input("enter any number: ")
 if n=="quit":
    print("terminate")
    break
 n=int(n)
 if n>0:
        print("positive number")
        continue
 elif n<0:
        print("negative number")
        continue
 else:
        print("Zero")
        continue
