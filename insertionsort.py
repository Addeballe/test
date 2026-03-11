import random
import time

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = []
for y in range(25000):
    arr.append(random.randint(1, 10000))

start_timer = time.time()
insertionSort(arr)
print(time.time() - start_timer)