print("The number of days in the school year is 180.")
a=int(input("Enter the number of days that you were present:"))
b=int(input("Enter the number of days taht you were absent:"))
c=a/180*100
if (c>=75) and (c>=100):
    print("Congratulations! You you have qualified to attend the exam!")
elif (c<75) and (c>=0):
    print("Unfortunately, it seems that you haven't qualified to attend the exam...")
else:
    print("Please enter a valid number of days present and absent.")
