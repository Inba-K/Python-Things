even=0
linenum=0
with open('Read.txt','r') as f:
    l=f.readlines()
    ln=len(l)
    for linenum in range(0,ln):
        linenum+=1
        if linenum%2==0:
            even+=1
print("There are",even,"even lines in the file.")
