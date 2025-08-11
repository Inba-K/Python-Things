def LCM(a, b):
    if a == 0 or b == 0:
        return 0
    
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1

c=int(input("Enter a number: "))
d=int(input("Enter another number: "))
lcm_result = LCM(c, d)
print(f"LCM of {c} and {d} is: {lcm_result}")
