a=int(input("Enter a number: "))
a=str(a)
b=a[::-1]
b=int(b)
a=int(a)
if a==b:
    print("Your number is a palindrome.")
else:
    print("Your number isn't a palindrome.")
