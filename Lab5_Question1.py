def candies(n, arr):
    candies = [1] * n
    
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)

def main():
   
    n = int(input("Enter the number of children in the class: "))
    arr = []
    print("Enter the ratings of each student:")
    for i in range(n):
        rating = int(input())
        arr.append(rating)

    print("Minimum number of candies Alice must buy:", candies(n, arr))

if __name__ == "__main__":
    main()
