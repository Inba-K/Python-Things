a=int(input("Enter a number: "))    

b=[]

for i in range(1,a+1):
    if a%i==0:
        b.append(i)

if len(b)==2:
    print("This number is prime!")
else:
    print("This number isn't prime.")
