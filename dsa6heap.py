def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def menu():
    arr = []
    while True:
        print("\n1. Enter array")
        print("2. Display array")
        print("3. Sort array")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
            print("Array saved.")

        elif choice == '2':
            print("Array:", arr if arr else "Empty")

        elif choice == '3':
            if not arr:
                print("Array is empty!")
            else:
                heap_sort(arr)
                print("Sorted array:", arr)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

menu()
