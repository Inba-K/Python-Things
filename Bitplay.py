
def find_all_duplications(a):
    duplicates=[]
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if(a[i]==a[j] and a[i] not in duplicates):
                duplicates.append(a[i])
                break
    return duplicates
a=[1,3,2,5,6,3,1]
b=find_all_duplications(a)
n=0
c=[]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j] and i&1 and b[j] not in c:
            c.append(b[j])
    n+=1
print(c,"is an odd occuring number.")
