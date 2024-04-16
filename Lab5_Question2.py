def maximumPeople(p, x, y, r):
    total_sunny_population = sum(p)
    
    for i in range(len(y)):
        cloud_range = set(range(y[i] - r[i], y[i] + r[i] + 1))
        total_dark_population = 0
        
        for j in range(len(x)):
            if x[j] in cloud_range:
                total_dark_population += p[j]
        
        total_sunny_population = max(total_sunny_population, total_sunny_population - total_dark_population)
    
    return total_sunny_population

def main():
    n = int(input("Enter the number of towns: "))
    
    p = list(map(int, input("Enter the populations of each town: ").split()))
    x = list(map(int, input("Enter the locations of each town: ").split()))
    
    m = int(input("Enter the number of clouds: "))
    
    y = list(map(int, input("Enter the locations of each cloud: ").split()))
    r = list(map(int, input("Enter the extents of each cloud: ").split()))
    
    print("Maximum number of people in a sunny town after removing exactly one cloud:", maximumPeople(p, x, y, r))

if __name__ == "__main__":
    main()
