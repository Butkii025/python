"""
Question:: let`s create a Number Guesssing Game ,
 given a secret number (already decided for you), 
 write a program that asks the user to guess it and print.
 .Too high== if no. is above
 .Too low== if no. is below
#  .corret== if matches"""

secret_number=7
guess=int(input("enter your guessed number: "))
if guess>secret_number:
    print("too high")
elif guess<secret_number:
    print("too low")
elif guess==secret_number:
    print("matched")
else:
    print("enter number only")

# we can do this same ques. using loop in which it will continously take value untill matches


while True:
 n=float(input("enter any number: "))
 i=9 # our guessed value
 if n==i: 
    print("matched")
    break
 if n>i:
        print("greater number")
        continue
 elif n<i:
        print("lower number")
        continue
 else:
        print("error, enter number only")
        continue


