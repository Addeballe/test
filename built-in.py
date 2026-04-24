import random
import time

arr = []
for y in range(25000):
    arr.append(random.randint(1, 10000))

start_timer = time.time()
arr.sort()

print(time.time() - start_timer)