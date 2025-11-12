#include <iostream>
#include <cctype>
using namespace std;

// Node structure for stack
struct Node {
    char data;
    Node* next;
};

// Stack ADT using linked list
class Stack {
private:
    Node* top;

public:
    Stack() {
        top = NULL;
    }

    void push(char value) {
        Node* newNode = new Node();
        newNode->data = value;
        newNode->next = top;
        top = newNode;
    }

    char pop() {
        if (isEmpty()) return '\0';
        Node* temp = top;
        char value = temp->data;
        top = top->next;
        delete temp;
        return value;
    }

    char peek() {
        if (isEmpty()) return '\0';
        return top->data;
    }

    bool isEmpty() {
        return top == NULL;
    }
};

// Check precedence of operators
int precedence(char op) {
    if (op == '^') return 3;
    if (op == '*' || op == '/') return 2;
    if (op == '+' || op == '-') return 1;
    return 0;
}

// Convert infix to postfix
string infixToPostfix(string infix) {
    Stack s;
    string postfix = "";

    for (char ch : infix) {
        if (isalnum(ch)) {
            postfix += ch;
        }
        else if (ch == '(') {
            s.push(ch);
        }
        else if (ch == ')') {
            while (!s.isEmpty() && s.peek() != '(')
                postfix += s.pop();
            s.pop(); // Remove '('
        }
        else {
            while (!s.isEmpty() && precedence(ch) <= precedence(s.peek()))
                postfix += s.pop();
            s.push(ch);
        }
    }

    while (!s.isEmpty())
        postfix += s.pop();

    return postfix;
}

// Main menu
int main() {
    int choice;
    string infix;

    do {
        cout << "\n--- MENU ---\n";
        cout << "1. Convert Infix to Postfix\n";
        cout << "2. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter infix expression (e.g., A+B*C): ";
            cin >> infix;
            string postfix = infixToPostfix(infix);
            cout << "Postfix Expression: " << postfix << "\n";
        }
        else if (choice == 2) {
            cout << "Exiting...\n";
        }
        else {
            cout << "Invalid choice. Try again.\n";
        }
    } while (choice != 2);

    return 0;
}--- MENU ---
1. Convert Infix to Postfix
2. Exit
Enter your choice: 1
Enter infix expression (e.g., A+B*C): A+B*C
Postfix Expression: ABC*+


