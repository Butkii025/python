# assignments

# Question 1: WAP that takes salary as an input. Using conditional statement calculate the final tax rate.

n=int(input(" enter your salary: "))
tax_amt=0
if (n<30000):
    tax_amt=n*5/100
    print("you tax amount is: ", tax_amt)

elif (n>=30000 and n<=70000):
    tax_amt=n*15/100
    print("your tax amount is: ",tax_amt)

elif (n>70000):
    tax_amt=n*25/100
    print("your tax amount is: ",tax_amt)
else:
    print("amount not correct")

