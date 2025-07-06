with open('Read.txt','r') as f:
    read=f.read()
with open('Intro.txt','r') as f:
    bead=f.read()
with open('Combine.txt','w') as f:
    f.write(read)
with open('Combine.txt','a') as f:
    f.write("\n")
with open('Combine.txt','a') as f:
    f.write(bead)
f=open('Combine.txt','r')
print(f.read())
f.close()
print("I had merged Intro.txt and Read.txt into Combine.txt.")
