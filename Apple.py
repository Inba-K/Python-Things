import time
import random
def myfunction(n):
    for i in range(0,n+1):
        print("First loop")
        j=1
        while (j>n+1):
            print("Second loop")
        
        for i in range(0,100):
            print("Third loop")
n=random.randint(0,100)
start=time.time()
myfunction(n)
end=time.time()
print(f"Time taken: {round((end-start)*1000,4)}ms")
