Grades={5,5,5,6,6,6,6,7,7,8,8,8,8,8,8,9,9,10,10,10,10,10,11,11,11,11,11,11,12,12,12,12,12,12}
a=input("Do you play basketball? ")
if a=='yes':
    b=int(input("What grade are you in? "))
    Grades.add(b)
    print("Kids who play basketball are in the grades", list(Grades))
else:
    print("Looks like you don't qualify for the survey.")
