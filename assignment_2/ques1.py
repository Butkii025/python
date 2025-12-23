# check palindrome

def is_palindrome(s):
    s=str(s)
    s=s.replace("","").lower()
    return s==s[::-1]
x=input("enter something: ")
if is_palindrome(x):
    print(f"{x} is palindrome")
else:
    print("no it`s not")