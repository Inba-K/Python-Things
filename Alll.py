import os

with open("A.txt","r") as f:
    a=f.readlines()
    for i in a:
        print(i.split())

if os.path.exists("B.txt"):
    print("B.txt exists!")
else:
    print("B.txt doesn't exist")
    f=open("B.txt","x")
print("Deleting B.txt...")
os.remove("B.txt")
print("B.txt successfully deleted.")

f=open('Read.txt','r')

print(f.read(9))

print(f.readline())
print(f.readline())

print(f.readlines())

for x in f:
    print(x)
