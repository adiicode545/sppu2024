def naive_string_match(text, pattern):
    """
    Naive string matching algorithm.
    Returns a list of starting indices where pattern is found in text.
    """
    n = len(text)
    m = len(pattern)
    indices = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            indices.append(i)

    return indices

def main():
    while True:
        print("\n--- Naive String Matching Menu ---")
        print("1. Perform String Matching")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            text = input("Enter the text string: ")
            pattern = input("Enter the pattern string: ")
            result = naive_string_match(text, pattern)

            if result:
                print(f"Pattern found at indices: {result}")
            else:
                print("Pattern not found in the text.")
        elif choice == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print("\n=== Code Execution Completed ===")

if __name__ == "__main__":
    main()
