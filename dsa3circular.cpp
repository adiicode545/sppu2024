#include<iostream>
using namespace std;

class Circular_Queue {
    int front, rear, size;
    int* queue;

public:
    Circular_Queue(int capacity) {
        size = capacity;
        queue = new int[size];  // corrected: use size in brackets
        front = rear = -1;
    }

    void enqueue(int value) {
        if ((rear + 1) % size == front) {
            cout << "Queue is full\n";
            return;
        }
        if (front == -1) {
            front = rear = 0;
        } else {
            rear = (rear + 1) % size;
        }
        queue[rear] = value;
        cout << "Inserted: " << value << endl;
    }

    void dequeue() {
        if (front == -1) {
            cout << "Queue is empty!\n";
            return;
        }
        cout << "Deleted: " << queue[front] << endl;
        if (front == rear) {  // corrected: use == not =
            front = rear = -1;
        } else {
            front = (front + 1) % size;
        }
    }

    void display() {
        if (front == -1) {
            cout << "Queue is empty\n";
            return;
        }

        cout << "Queue elements:\n";
        int i = front;
        while (true) {
            cout << queue[i] << " ";
            if (i == rear) break;  // corrected: use == not =
            i = (i + 1) % size;
        }
        cout << endl;
    }
};

int main() {
    int capacity;
    cout << "Enter the capacity of Queue: ";
    cin >> capacity;

    Circular_Queue cq(capacity);
    int choice, value;

    while (true) {  // corrected: use lowercase true
        cout << "\n--- Circular Queue Menu ---\n";
        cout << "1. Enqueue\n";
        cout << "2. Dequeue\n";
        cout << "3. Display\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter value to insert: ";
            cin >> value;
            cq.enqueue(value);
        } else if (choice == 2) {
            cq.dequeue();
        } else if (choice == 3) {
            cq.display();
        } else if (choice == 4) {
            cout << "Exiting...\n";
            break;
        } else {
            cout << "Invalid choice.\n";
        }
    }

    return 0;
}
