import random
import time

def partition(arr, low, high):
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    if low < high:
        
        pi = partition(arr, low, high)
        
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

arr = []
for y in range(5000):
    arr.append(random.randint(1, 10000))
n = len(arr)

start_timer = time.time()
quickSort(arr, 0, n - 1)
print(time.time() - start_timer)