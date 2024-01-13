import timeit
import random
from tabulate import tabulate

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def timsort(arr):
    return sorted(arr)

def generate_random_list(length):
    return [random.randint(0, 1000) for _ in range(length)]

def measure_time(sort_func, data):
    start_time = timeit.default_timer()
    sort_func(data)
    elapsed_time = (timeit.default_timer() - start_time) * 1000  
    return elapsed_time

results = []

for size in [10, 100, 1000, 10000]:
    data = generate_random_list(size)
    
    merge_time = measure_time(merge_sort, data.copy())
    insertion_time = measure_time(insertion_sort, data.copy())
    timsort_time = measure_time(timsort, data.copy())

    fastest_time = min(merge_time, insertion_time, timsort_time)

    results.append([size, f"{merge_time:.3f}", f"{insertion_time:.3f}", f"{timsort_time:.3f}", f"{fastest_time:.3f}"])

headers = ["Розмір списку", "Злиття (мс)", "Вставки (мс)", "Timsort (мс)", "Найшвидший (мс)"]
table = tabulate(results, headers=headers, tablefmt="pipe", floatfmt=".3f", numalign="right")

print(table)