with open('Read.txt','r') as f:
    read=f.read()
with open('Cool.txt','w') as f:
    f.write("My name is Inba, and I have something to tell you.\n")
with open('Cool.txt','a') as f:
    f.write(read)
with open('Cool.txt','r') as f:
    print(f.read())
