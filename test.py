import random
import time

def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

arr = []
for y in range(25000):
    arr.append(random.randint(1, 10000))

start_timer = time.time()
bubbleSort(arr)

#print("Sorted array:")
#for i in range(len(arr)):
    #print("%d" % arr[i], end=" ")
print(time.time() - start_timer)