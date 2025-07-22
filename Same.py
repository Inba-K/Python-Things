import random
import time

def myfunction1(n):
    if n>0:
        return n
    for i in range(0,n+1):
        print("Codingal")
    myfunction1(n/2)
    myfunction1(n/3)
def myfunction2(n):
    if n<=1:
        return n
    print("Codingal")
    myfunction2(n-1)
a=10*5
n=random.choice(range(a))
start=time.time()
myfunction1(n)
myfunction2(n)
end=time.time()
print(f"Time taken: {round((end-start),4)}ms")
