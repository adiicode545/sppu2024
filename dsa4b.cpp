#include <iostream>
#include <queue>
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

// Insert node
Node* insert(Node* root, int value) {
    if (root == NULL)
        return createNode(value);
    if (value < root->data)
        root->left = insert(root->left, value);
    else if (value > root->data)
        root->right = insert(root->right, value);
    else
        cout << "Duplicate not allowed: " << value << "\n";
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

// Mirror image
Node* mirror(Node* root) {
    if (root == NULL)
        return NULL;
    Node* temp = new Node();
    temp->data = root->data;
    temp->left = mirror(root->right);
    temp->right = mirror(root->left);
    return temp;
}

// Copy tree
Node* copyTree(Node* root) {
    if (root == NULL)
        return NULL;
    Node* newNode = new Node();
    newNode->data = root->data;
    newNode->left = copyTree(root->left);
    newNode->right = copyTree(root->right);
    return newNode;
}

// Display parent and children
void displayParents(Node* root) {
    if (root != NULL) {
        if (root->left || root->right) {
            cout << "Parent: " << root->data << " -> ";
            if (root->left)
                cout << "Left Child: " << root->left->data << " ";
            if (root->right)
                cout << "Right Child: " << root->right->data;
            cout << "\n";
        }
        displayParents(root->left);
        displayParents(root->right);
    }
}

// Display leaf nodes
void displayLeaves(Node* root) {
    if (root != NULL) {
        if (root->left == NULL && root->right == NULL)
            cout << root->data << " ";
        displayLeaves(root->left);
        displayLeaves(root->right);
    }
}

// Level-wise display
void levelOrder(Node* root) {
    if (root == NULL)
        return;
    queue<Node*> q;
    q.push(root);
    cout << "Level-wise display:\n";
    while (!q.empty()) {
        Node* temp = q.front();
        q.pop();
        cout << temp->data << " ";
        if (temp->left)
            q.push(temp->left);
        if (temp->right)
            q.push(temp->right);
    }
    cout << "\n";
}

// Main menu
int main() {
    Node* root = NULL;
    Node* mirrorRoot = NULL;
    Node* copyRoot = NULL;
    int choice, value;

    do {
        cout << "\n--- BST MENU ---\n";
        cout << "1. Insert\n";
        cout << "2. Display Inorder\n";
        cout << "3. Display Mirror Image\n";
        cout << "4. Create and Display Copy\n";
        cout << "5. Display Parent Nodes with Children\n";
        cout << "6. Display Leaf Nodes\n";
        cout << "7. Display Tree Level-wise\n";
        cout << "8. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter value to insert: ";
            cin >> value;
            root = insert(root, value);
        }
        else if (choice == 2) {
            cout << "Inorder Traversal: ";
            inorder(root);
            cout << "\n";
        }
        else if (choice == 3) {
            mirrorRoot = mirror(root);
            cout << "Mirror Image (Inorder): ";
            inorder(mirrorRoot);
            cout << "\n";
        }
        else if (choice == 4) {
            copyRoot = copyTree(root);
            cout << "Copied Tree (Inorder): ";
            inorder(copyRoot);
            cout << "\n";
        }
        else if (choice == 5) {
            displayParents(root);
        }
        else if (choice == 6) {
            cout << "Leaf Nodes: ";
            displayLeaves(root);
            cout << "\n";
        }
        else if (choice == 7) {
            levelOrder(root);
        }
        else if (choice == 8) {
            cout << "Exiting...\n";
        }
        else {
            cout << "Invalid choice. Try again.\n";
        }
    } while (choice != 8);

    return 0;
}

You got it, Soham! Here's a complete, exam-ready C++ program that implements a Binary Search Tree (BST) and performs all the operations listed in Question 4B:
________________________________________
✅ Operations Covered
•	f. Mirror image
•	g. Create a copy
•	h. Display parent nodes with child nodes
•	i. Display leaf nodes
•	j. Display tree level-wise
________________________________________
🌳 C++ Code: BST with All Operations
#include <iostream>
#include <queue>
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

// Insert node
Node* insert(Node* root, int value) {
    if (root == NULL)
        return createNode(value);
    if (value < root->data)
        root->left = insert(root->left, value);
    else if (value > root->data)
        root->right = insert(root->right, value);
    else
        cout << "Duplicate not allowed: " << value << "\n";
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

// Mirror image
Node* mirror(Node* root) {
    if (root == NULL)
        return NULL;
    Node* temp = new Node();
    temp->data = root->data;
    temp->left = mirror(root->right);
    temp->right = mirror(root->left);
    return temp;
}

// Copy tree
Node* copyTree(Node* root) {
    if (root == NULL)
        return NULL;
    Node* newNode = new Node();
    newNode->data = root->data;
    newNode->left = copyTree(root->left);
    newNode->right = copyTree(root->right);
    return newNode;
}

// Display parent and children
void displayParents(Node* root) {
    if (root != NULL) {
        if (root->left || root->right) {
            cout << "Parent: " << root->data << " -> ";
            if (root->left)
                cout << "Left Child: " << root->left->data << " ";
            if (root->right)
                cout << "Right Child: " << root->right->data;
            cout << "\n";
        }
        displayParents(root->left);
        displayParents(root->right);
    }
}

// Display leaf nodes
void displayLeaves(Node* root) {
    if (root != NULL) {
        if (root->left == NULL && root->right == NULL)
            cout << root->data << " ";
        displayLeaves(root->left);
        displayLeaves(root->right);
    }
}

// Level-wise display
void levelOrder(Node* root) {
    if (root == NULL)
        return;
    queue<Node*> q;
    q.push(root);
    cout << "Level-wise display:\n";
    while (!q.empty()) {
        Node* temp = q.front();
        q.pop();
        cout << temp->data << " ";
        if (temp->left)
            q.push(temp->left);
        if (temp->right)
            q.push(temp->right);
    }
    cout << "\n";
}

// Main menu
int main() {
    Node* root = NULL;
    Node* mirrorRoot = NULL;
    Node* copyRoot = NULL;
    int choice, value;

    do {
        cout << "\n--- BST MENU ---\n";
        cout << "1. Insert\n";
        cout << "2. Display Inorder\n";
        cout << "3. Display Mirror Image\n";
        cout << "4. Create and Display Copy\n";
        cout << "5. Display Parent Nodes with Children\n";
        cout << "6. Display Leaf Nodes\n";
        cout << "7. Display Tree Level-wise\n";
        cout << "8. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter value to insert: ";
            cin >> value;
            root = insert(root, value);
        }
        else if (choice == 2) {
            cout << "Inorder Traversal: ";
            inorder(root);
            cout << "\n";
        }
        else if (choice == 3) {
            mirrorRoot = mirror(root);
            cout << "Mirror Image (Inorder): ";
            inorder(mirrorRoot);
            cout << "\n";
        }
        else if (choice == 4) {
            copyRoot = copyTree(root);
            cout << "Copied Tree (Inorder): ";
            inorder(copyRoot);
            cout << "\n";
        }
        else if (choice == 5) {
            displayParents(root);
        }
        else if (choice == 6) {
            cout << "Leaf Nodes: ";
            displayLeaves(root);
            cout << "\n";
        }
        else if (choice == 7) {
            levelOrder(root);
        }
        else if (choice == 8) {
            cout << "Exiting...\n";
        }
        else {
            cout << "Invalid choice. Try again.\n";
        }
    } while (choice != 8);

    return 0;
}
________________________________________
🧪 Sample Interaction
Enter value to insert: 50
Enter value to insert: 30
Enter value to insert: 70
Enter value to insert: 20
Enter value to insert: 40
Enter value to insert: 60
Enter value to insert: 80

Inorder Traversal: 20 30 40 50 60 70 80
Mirror Image (Inorder): 80 70 60 50 40 30 20
Copied Tree (Inorder): 20 30 40 50 60 70 80
Parent: 50 -> Left Child: 30 Right Child: 70
Parent: 30 -> Left Child: 20 Right Child: 40
Parent: 70 -> Left Child: 60 Right Child: 80
Leaf Nodes: 20 40 60 80
Level-wise display:
50 30 70 20 40 60 80
________________________________________
Let me know if you want this visualized or converted to Python for practice!

