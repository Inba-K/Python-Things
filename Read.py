f=open('Read.txt','r')

print(f.read(9))

print(f.readline())
print(f.readline())

print(f.readlines())

for x in f:
    print(x)
