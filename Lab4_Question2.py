def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def maximize_sum(arr):
    
    selection_sort(arr)

    
    total_sum = 0

    for i in range(len(arr)):
        total_sum += arr[i] * i

    return total_sum

arr = list(map(int, input("Enter the array of integers separated by space: ").split()))

max_sum = maximize_sum(arr)
print("Maximum sum:", max_sum)
