a=int(input("Enter a number: "))
b=[True]*(a+1)
c=2

while c*c<=a:
    if b[c]:
        for i in range(c*c,a+1,c):
            b[i]=False
    c+=1
d=[]

for c in range(2,a+1):
    if b[c]:
        d.append(c)

print(d)
