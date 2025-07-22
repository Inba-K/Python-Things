import time
import random
def function(arr,target):
    left,right=0,len(arr)
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

n=10*9
arr=list(range(n))
target=random.choice(arr)
start=time.time()
function(arr,target)
end=time.time()
print(f"Time taken:{round(end-start,8)}seconds")
