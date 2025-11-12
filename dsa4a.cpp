#include <iostream>
using namespace std;

// Node structure
struct Node {
    int data;
    Node* left;
    Node* right;
};

// Create new node
Node* createNode(int value) {
    Node* newNode = new Node();
    newNode->data = value;
    newNode->left = newNode->right = NULL;
    return newNode;
}

// Insert node (no duplicates)
Node* insert(Node* root, int value) {
    if (root == NULL)
        return createNode(value);
    if (value < root->data)
        root->left = insert(root->left, value);
    else if (value > root->data)
        root->right = insert(root->right, value);
    else
        cout << "Duplicate entry not allowed: " << value << "\n";
    return root;
}

// Search node
bool search(Node* root, int value) {
    if (root == NULL)
        return false;
    if (value == root->data)
        return true;
    else if (value < root->data)
        return search(root->left, value);
    else
        return search(root->right, value);
}

// Find minimum value node
Node* findMin(Node* root) {
    while (root->left != NULL)
        root = root->left;
    return root;
}

// Delete node
Node* deleteNode(Node* root, int value) {
    if (root == NULL)
        return root;
    if (value < root->data)
        root->left = deleteNode(root->left, value);
    else if (value > root->data)
        root->right = deleteNode(root->right, value);
    else {
        // Node with one or no child
        if (root->left == NULL) {
            Node* temp = root->right;
            delete root;
            return temp;
        }
        else if (root->right == NULL) {
            Node* temp = root->left;
            delete root;
            return temp;
        }
        // Node with two children
        Node* temp = findMin(root->right);
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}

// Inorder traversal
void inorder(Node* root) {
    if (root != NULL) {
        inorder(root->left);
        cout << root->data << " ";
        inorder(root->right);
    }
}

// Calculate depth
int depth(Node* root) {
    if (root == NULL)
        return 0;
    int leftDepth = depth(root->left);
    int rightDepth = depth(root->right);
    return max(leftDepth, rightDepth) + 1;
}

// Main menu
int main() {
    Node* root = NULL;
    int choice, value;

    do {
        cout << "\n--- BST MENU ---\n";
        cout << "1. Insert\n";
        cout << "2. Delete\n";
        cout << "3. Search\n";
        cout << "4. Display (Inorder Traversal)\n";
        cout << "5. Display Depth of Tree\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter value to insert: ";
            cin >> value;
            root = insert(root, value);
        }
        else if (choice == 2) {
            cout << "Enter value to delete: ";
            cin >> value;
            root = deleteNode(root, value);
        }
        else if (choice == 3) {
            cout << "Enter value to search: ";
            cin >> value;
            if (search(root, value))
                cout << "Value found in BST.\n";
            else
                cout << "Value not found.\n";
        }
        else if (choice == 4) {
            cout << "Inorder Traversal: ";
            inorder(root);
            cout << "\n";
        }
        else if (choice == 5) {
            cout << "Depth of Tree: " << depth(root) << "\n";
        }
        else if (choice == 6) {
            cout << "Exiting...\n";
        }
        else {
            cout << "Invalid choice. Try again.\n";
        }
    } while (choice != 6);

    return 0;
}

Here’s a **complete, exam-ready C++ program** that implements a **Binary Search Tree (BST)** with all the required operations:

- ✅ Insert (with duplicate handling)
- ✅ Delete
- ✅ Search
- ✅ Display (Inorder Traversal)
- ✅ Display Depth of Tree

---

### 🌳 C++ Code: Binary Search Tree with Menu

```cpp
#include <iostream>
using namespace std;

// Node structure
struct Node {
    int data;
    Node* left;
    Node* right;
};

// Create new node
Node* createNode(int value) {
    Node* newNode = new Node();
    newNode->data = value;
    newNode->left = newNode->right = NULL;
    return newNode;
}

// Insert node (no duplicates)
Node* insert(Node* root, int value) {
    if (root == NULL)
        return createNode(value);
    if (value < root->data)
        root->left = insert(root->left, value);
    else if (value > root->data)
        root->right = insert(root->right, value);
    else
        cout << "Duplicate entry not allowed: " << value << "\n";
    return root;
}

// Search node
bool search(Node* root, int value) {
    if (root == NULL)
        return false;
    if (value == root->data)
        return true;
    else if (value < root->data)
        return search(root->left, value);
    else
        return search(root->right, value);
}

// Find minimum value node
Node* findMin(Node* root) {
    while (root->left != NULL)
        root = root->left;
    return root;
}

// Delete node
Node* deleteNode(Node* root, int value) {
    if (root == NULL)
        return root;
    if (value < root->data)
        root->left = deleteNode(root->left, value);
    else if (value > root->data)
        root->right = deleteNode(root->right, value);
    else {
        // Node with one or no child
        if (root->left == NULL) {
            Node* temp = root->right;
            delete root;
            return temp;
        }
        else if (root->right == NULL) {
            Node* temp = root->left;
            delete root;
            return temp;
        }
        // Node with two children
        Node* temp = findMin(root->right);
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}

// Inorder traversal
void inorder(Node* root) {
    if (root != NULL) {
        inorder(root->left);
        cout << root->data << " ";
        inorder(root->right);
    }
}

// Calculate depth
int depth(Node* root) {
    if (root == NULL)
        return 0;
    int leftDepth = depth(root->left);
    int rightDepth = depth(root->right);
    return max(leftDepth, rightDepth) + 1;
}

// Main menu
int main() {
    Node* root = NULL;
    int choice, value;

    do {
        cout << "\n--- BST MENU ---\n";
        cout << "1. Insert\n";
        cout << "2. Delete\n";
        cout << "3. Search\n";
        cout << "4. Display (Inorder Traversal)\n";
        cout << "5. Display Depth of Tree\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter value to insert: ";
            cin >> value;
            root = insert(root, value);
        }
        else if (choice == 2) {
            cout << "Enter value to delete: ";
            cin >> value;
            root = deleteNode(root, value);
        }
        else if (choice == 3) {
            cout << "Enter value to search: ";
            cin >> value;
            if (search(root, value))
                cout << "Value found in BST.\n";
            else
                cout << "Value not found.\n";
        }
        else if (choice == 4) {
            cout << "Inorder Traversal: ";
            inorder(root);
            cout << "\n";
        }
        else if (choice == 5) {
            cout << "Depth of Tree: " << depth(root) << "\n";
        }
        else if (choice == 6) {
            cout << "Exiting...\n";
        }
        else {
            cout << "Invalid choice. Try again.\n";
        }
    } while (choice != 6);

    return 0;
}
```

---

### 🧪 Sample Interaction

```
--- BST MENU ---
1. Insert
2. Delete
3. Search
4. Display (Inorder Traversal)
5. Display Depth of Tree
6. Exit
Enter your choice: 1
Enter value to insert: 50

Enter your choice: 1
Enter value to insert: 30

Enter your choice: 1
Enter value to insert: 70

Enter your choice: 1
Enter value to insert: 30
Duplicate entry not allowed: 30

Enter your choice: 4
Inorder Traversal: 30 50 70

Enter your choice: 5
Depth of Tree: 2

Enter your choice: 2
Enter value to delete: 50

Enter your choice: 4
Inorder Traversal: 30 70
```

---

Let me know if you want this converted to a **menu-driven Python version** or visualized with tree diagrams for viva prep!
