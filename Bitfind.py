num=int(input("Enter a number: "))
binary=""
n=num
while n>0:
    binary=str(n%2)+binary
    n=n//2

for i in range(0,len(binary)):
    if binary[i]=="1":
        print(i,"instance(s) found.")
