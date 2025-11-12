def fractional_knapsack(weights, profits, capacity):
    """
    Solves the fractional knapsack problem using greedy strategy.
    Returns the maximum profit that can be earned.
    """
    n = len(weights)  # Number of parcels

    # Step 1: Calculate profit-to-weight ratio for each parcel
    ratio = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(n)]

    # Step 2: Sort parcels by ratio in descending order
    ratio.sort(reverse=True, key=lambda x: x[0])

    total_profit = 0.0  # Initialize total profit

    # Step 3: Pick parcels greedily
    for r, w, p in ratio:
        if capacity == 0:
            break  # Stop if truck is full

        if w <= capacity:
            # Take full parcel
            total_profit += p
            capacity -= w
        else:
            # Take fraction of parcel
            total_profit += r * capacity
            capacity = 0

    return total_profit  # Return final profit

def main():
    while True:
        # Display menu
        print("\n--- Fractional Knapsack Menu ---")
        print("1. Enter Parcels and Capacity (User Input)")
        print("2. Exit")

        choice = int(input("Enter choice: "))

        match choice:
            case 1:
                # Input number of parcels
                n = int(input("Enter number of parcels: "))
                weights = []
                profits = []

                # Input weight and profit for each parcel
                for i in range(n):
                    print(f"\n--- Parcel {i+1} ---")
                    w = int(input("Enter weight: "))
                    p = int(input("Enter profit: "))
                    weights.append(w)
                    profits.append(p)

                # Input truck capacity
                capacity = int(input("\nEnter truck capacity: "))

                # Calculate max profit
                max_profit = fractional_knapsack(weights, profits, capacity)

                # Display result
                print("\n--- Result ---")
                for i in range(n):
                    print(f"Parcel {i+1}: Weight = {weights[i]}, Profit = {profits[i]}")
                print(f"\nTruck Capacity: {capacity}")
                print(f"Maximum Profit: {max_profit}\n")

            case 2:
                print("Exiting...")
                break

            case _:
                print("Invalid choice, try again.\n")

# Run the program
main()
