# ---------- Binary Search Tree Implementation ----------

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # ---------- Insert a new node ----------
    def insert(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            print(f"Duplicate key {key} not allowed.")
        return root

    # ---------- Search a key ----------
    def search(self, root, key):
        if root is None:
            return None
        if key == root.key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # ---------- Find minimum value node (used in deletion) ----------
    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # ---------- Delete a node ----------
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children:
            # Get inorder successor (smallest in the right subtree)
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    # ---------- Display: Traversals ----------
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

# ---------- Main Program ----------
if __name__ == "__main__":
    bst = BST()
    root = None

    while True:
        print("\n--- Binary Search Tree Operations ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display (Inorder / Preorder / Postorder)")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter value to insert: "))
            root = bst.insert(root, key)
        elif choice == 2:
            key = int(input("Enter value to delete: "))
            root = bst.delete(root, key)
        elif choice == 3:
            key = int(input("Enter value to search: "))
            result = bst.search(root, key)
            if result:
                print(f"Key {key} found in the BST.")
            else:
                print(f"Key {key} not found in the BST.")
        elif choice == 4:
            print("\nInorder Traversal  : ", end="")
            bst.inorder(root)
            print("\nPreorder Traversal : ", end="")
            bst.preorder(root)
            print("\nPostorder Traversal: ", end="")
            bst.postorder(root)
            print()
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")
