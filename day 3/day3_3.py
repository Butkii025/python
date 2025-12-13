# for loops

for i in range(3):
    print("vijju")

# count of i in word

word= " artificial intelligence"

ans=0
for ch in word:
    if (ch =="i"):
        ans+=1
        print("count of I is:",ans )

# WAP  to print the sum of first "n" natural numbers 

#1+2+3+4+5
n=int(input("enter no: "))
sum=0

for i in range(1, n+1):
    sum += i
    print(" sum =", sum)