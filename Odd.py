odd=0
linenum=0
with open('Read.txt','r') as f:
    l=f.readlines()
    ln=len(l)
    for linenum in range(0,ln+1):
        linenum+=1
        if linenum%2!=0:
            odd+=1
print("There are",odd,"odd lines in the file.")
