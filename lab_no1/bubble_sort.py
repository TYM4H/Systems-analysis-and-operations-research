import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[i]
    return arr

sizes = [1000, 2000, 5000, 10000]

for n in sizes:
    arr = [random.randint(0, 10000) for _ in range(n)]
    
    # Пузырьковая сортировка
    arr_copy = arr.copy()
    start_time = time.time()
    bubble_sort(arr_copy)
    bubble_time = time.time() - start_time
    
    # Встроенная сортировка
    arr_copy2 = arr.copy()
    start_time = time.time()
    sorted(arr_copy2)
    built_in_time = time.time() - start_time
    
    print(f"n={n}: Bubble sort = {bubble_time:.6f}s, Python sorted() = {built_in_time:.6f}s")

