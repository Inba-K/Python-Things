def fibonacci_sequence():
    a=0
    b=1
    while a<5000:
        print("\n",a)
        a, b = b, a + b
print(fibonacci_sequence())
