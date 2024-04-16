def fractional_knapsack(items, capacity):
    
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0
    sack = []

    for benefit, weight in items:
        if capacity == 0:
            break
        fraction = min(1, capacity / weight)
        total_value += fraction * benefit
        sack.append((benefit, weight, fraction))
        capacity -= fraction * weight

    return total_value, sack

def main():
    
    num_items = int(input("Enter the number of items: "))
    items = []
    for i in range(num_items):
        benefit, weight = map(int, input(f"Enter benefit and weight for item {i+1}: ").split())
        items.append((benefit, weight))
    capacity = int(input("Enter the sack capacity: "))

   
    max_value, sack = fractional_knapsack(items, capacity)
    print("\nOptimal Solution:")
    print("Maximum value in the sack:", max_value)
    print("Items in the sack:")
    for item in sack:
        print("  Benefit:", item[0], "| Weight:", item[1], "| Fraction taken:", item[2])

if __name__ == "__main__":
    main()
