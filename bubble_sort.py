import random
import time
import pandas as pd
import matplotlib.pyplot as plt
def bubble_sort(arr):#bubble sort
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def merge_sort(arr):#merge sort
    if len(arr) > 1:
        mid = len(arr) // 2  
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def quick_sort(arr):#quick sort
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
array_sizes = [100, 500, 1000, 5000]
results = []
for size in array_sizes:
    print(f"Benchmarking array size: {size}")
    base_array = random.sample(range(1, size * 10), size)
    arr = base_array.copy()
    start = time.time()
    bubble_sort(arr)
    end = time.time()
    bubble_time = end - start
    arr = base_array.copy()
    start = time.time()
    merge_sort(arr)
    end = time.time()
    merge_time = end - start
    arr = base_array.copy()
    start = time.time()
    quick_sort(arr)
    end = time.time()
    quick_time = end - start
    results.append({
        'Array Size': size,
        'Bubble Sort Time': bubble_time,
        'Merge Sort Time': merge_time,
        'Quick Sort Time': quick_time
    })
df = pd.DataFrame(results)
print("\nBenchmark Results:\n")
print(df)
plt.figure(figsize=(10, 6))
bar_width = 0.25
x = range(len(df))
plt.bar([i - bar_width for i in x], df['Bubble Sort Time'], width=bar_width, label='Bubble Sort')
plt.bar(x, df['Merge Sort Time'], width=bar_width, label='Merge Sort')
plt.bar([i + bar_width for i in x], df['Quick Sort Time'], width=bar_width, label='Quick Sort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Sorting Algorithm Time Comparison')
plt.xticks(ticks=x, labels=df['Array Size'])
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("benchmark_plot.png")
plt.show()
