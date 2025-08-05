def Translate(b):
    d,p=0,0
    while b:
        d+=(b % 10)*(2 ** p)
        b//=10
        p+=1
    print(d)
a=int(input("Enter binary: "))
for num in [a]:
    Translate(num)
