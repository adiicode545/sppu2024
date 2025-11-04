
class CityNode:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.left = None
        self.right = None

class CityBST:
    def __init__(self):
        self.root = None

    # Insert a new city into BST
    def insert(self, root, name, population):
        if root is None:
            return CityNode(name, population)
        if name.lower() < root.name.lower():
            root.left = self.insert(root.left, name, population)
        elif name.lower() > root.name.lower():
            root.right = self.insert(root.right, name, population)
        else:
            print(f"City '{name}' already exists. Use update option instead.")
        return root

    # Search for a city and count comparisons
    def search(self, root, name, comparisons=0):
        if root is None:
            return None, comparisons
        comparisons += 1
        if name.lower() == root.name.lower():
            return root, comparisons
        elif name.lower() < root.name.lower():
            return self.search(root.left, name, comparisons)
        else:
            return self.search(root.right, name, comparisons)

    # Update population of a city
    def update_population(self, root, name, new_population):
        city, _ = self.search(root, name)
        if city:
            city.population = new_population
            print(f"Population of '{name}' updated to {new_population}.")
        else:
            print(f"City '{name}' not found.")

    # Find the minimum value node (used in deletion)
    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Delete a city
    def delete(self, root, name):
        if root is None:
            return root
        if name.lower() < root.name.lower():
            root.left = self.delete(root.left, name)
        elif name.lower() > root.name.lower():
            root.right = self.delete(root.right, name)
        else:
            # Node with one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children
            temp = self.minValueNode(root.right)
            root.name = temp.name
            root.population = temp.population
            root.right = self.delete(root.right, temp.name)
        return root

    # Display cities in ascending order
    def display_ascending(self, root):
        if root:
            self.display_ascending(root.left)
            print(f"{root.name}: {root.population}")
            self.display_ascending(root.right)

    # Display cities in descending order
    def display_descending(self, root):
        if root:
            self.display_descending(root.right)
            print(f"{root.name}: {root.population}")
            self.display_descending(root.left)

    # Count maximum comparisons (equal to tree height)
    def max_comparisons(self, root):
        if root is None:
            return 0
        left_height = self.max_comparisons(root.left)
        right_height = self.max_comparisons(root.right)
        return 1 + max(left_height, right_height)

# --- Main Program ---
bst = CityBST()

while True:
    print("\n--- City Management System ---")
    print("1. Add a new city")
    print("2. Delete a city")
    print("3. Update population")
    print("4. Display cities in ascending order")
    print("5. Display cities in descending order")
    print("6. Search for a city")
    print("7. Show maximum comparisons required for search")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        name = input("Enter city name: ")
        population = int(input("Enter population: "))
        bst.root = bst.insert(bst.root, name, population)

    elif choice == '2':
        name = input("Enter city name to delete: ")
        bst.root = bst.delete(bst.root, name)

    elif choice == '3':
        name = input("Enter city name to update: ")
        new_pop = int(input("Enter new population: "))
        bst.update_population(bst.root, name, new_pop)

    elif choice == '4':
        print("\nCities in ascending order:")
        bst.display_ascending(bst.root)

    elif choice == '5':
        print("\nCities in descending order:")
        bst.display_descending(bst.root)

    elif choice == '6':
        name = input("Enter city name to search: ")
        city, comps = bst.search(bst.root, name)
        if city:
            print(f"City found: {city.name}, Population: {city.population}")
            print(f"Comparisons made: {comps}")
        else:
            print(f"City '{name}' not found after {comps} comparisons.")

    elif choice == '7':
        max_comps = bst.max_comparisons(bst.root)
        print(f"Maximum comparisons required to search for any city: {max_comps}")

    elif choice == '8':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
