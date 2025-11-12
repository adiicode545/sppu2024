def merge(left, right, show_steps):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    if show_steps:
        print("Merging step:", result)
    return result

def merge_sort(orders, show_steps):
    if len(orders) <= 1:
        return orders
    mid = len(orders) // 2
    left = merge_sort(orders[:mid], show_steps)
    right = merge_sort(orders[mid:], show_steps)
    return merge(left, right, show_steps)

def main():
    orders = []
    while True:
        print("\n--- MENU ---")
        print("1. Enter Orders")
        print("2. Show Orders")
        print("3. Sort Orders by Delivery Time")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            orders.clear()
            n = int(input("How many orders? "))
            for i in range(n):
                oid = input(f"Order ID #{i+1}: ")
                time = int(input(f"Delivery Time for {oid}: "))
                orders.append((oid, time))
            print("Orders added.")

        elif choice == '2':
            if not orders:
                print("No orders to show.")
            else:
                print("Current Orders:")
                for oid, time in orders:
                    print(f"{oid} - {time} min")

        elif choice == '3':
            if not orders:
                print("No orders to sort.")
            else:
                show = input("Show merge steps? (1 = Yes, 0 = No): ")
                show_steps = (show == '1')
                sorted_orders = merge_sort(orders, show_steps)
                print("Sorted Orders:")
                for oid, time in sorted_orders:
                    print(f"{oid} - {time} min")

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
