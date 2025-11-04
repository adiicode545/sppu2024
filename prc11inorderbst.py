
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a node into the BST
    def insert(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            print("Duplicate key not allowed:", key)
        return root

    # Search a node in the BST
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    # Find the minimum value node (used in deletion)
    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Delete a node from BST
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

            # Node with two children: get inorder successor
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    # Display BST (Inorder Traversal)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

# --- Main Program ---
bst = BinarySearchTree()

# Insert nodes
for key in [50, 30, 20, 40, 70, 60, 80]:
    bst.root = bst.insert(bst.root, key)

print("Inorder traversal of BST:")
bst.inorder(bst.root)
print()

# Search operation
key = 40
if bst.search(bst.root, key):
    print(f"Key {key} found in BST.")
else:
    print(f"Key {key} not found in BST.")

# Delete operation
key_to_delete = 20
bst.root = bst.delete(bst.root, key_to_delete)
print(f"\nBST after deleting {key_to_delete}:")
bst.inorder(bst.root)
print()
