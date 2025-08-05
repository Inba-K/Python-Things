def Roman(enter):
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    r=0
    for i in range(0, len(enter)-1):
        if roman[enter[i]]<roman[enter[i+1]]:
            r=roman[enter[i]]
        else:
            r+=roman[enter[i]]
    return r+roman[enter[-1]]
roman=input("Enter a Roman numeral: ")
print("Integer equivalent:",Roman(roman))
