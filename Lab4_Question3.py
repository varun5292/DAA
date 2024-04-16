def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def minimize_sum_product(arr1, arr2):
  
    selection_sort(arr1)
    selection_sort(arr2)

    arr2.reverse()

    total_sum = sum(arr1[i] * arr2[i] for i in range(len(arr1)))

    return total_sum


arr1 = list(map(int, input("Enter the first array of integers separated by space: ").split()))
arr2 = list(map(int, input("Enter the second array of integers separated by space: ").split()))


min_sum_product = minimize_sum_product(arr1, arr2)
print("Minimum sum of product:", min_sum_product)
