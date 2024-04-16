def pylons(k, arr):
    n = len(arr)
    count = 0
    i = 0
    
    while i < n:
        j = min(i + k - 1, n - 1)
        while j >= i - k + 1 and arr[j] == 0:
            j -= 1
        if j < i - k + 1:
            return -1
        count += 1
        i = j + k
    
    return count

# User input
n, k = map(int, input("Enter the number of cities and the plants' range constant (separated by space): ").split())
arr = list(map(int, input("Enter the binary integers indicating suitability for building a plant (separated by space): ").split()))

# Output
result = pylons(k, arr)
if result == -1:
    print("It is not possible to provide electricity to all cities with the given distribution constraint.")
else:
    print("The minimum number of plants required to provide electricity to all cities:", result)
