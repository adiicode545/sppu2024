
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

struct Student {
    int id;
    char name[50];
    float cgpa;
};

void addStudent(Student*& students, int& size, int& capacity) {
    if (size >= capacity) {
        capacity *= 2;
        Student* temp = new Student[capacity];
        for (int i = 0; i < size; i++)
            temp[i] = students[i];
        delete[] students;
        students = temp;
    }

    cout << "Enter ID: ";
    cin >> students[size].id;
    cout << "Enter Name: ";
    cin.ignore();
    cin.getline(students[size].name, 50);
    cout << "Enter CGPA: ";
    cin >> students[size].cgpa;
    size++;
}

int binarySearch(Student* students, int size, int targetID) {
    int low = 0, high = size - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (students[mid].id == targetID)
            return mid;
        else if (students[mid].id < targetID)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

void bubbleSortByName(Student* students, int size) {
    for (int i = 0; i < size - 1; i++)
        for (int j = 0; j < size - i - 1; j++)
            if (strcmp(students[j].name, students[j + 1].name) > 0)
                swap(students[j], students[j + 1]);
}

void insertionSortByCGPA(Student* students, int size, bool ascending) {
    for (int i = 1; i < size; i++) {
        Student key = students[i];
        int j = i - 1;
        while (j >= 0 && ((ascending && students[j].cgpa > key.cgpa) ||
                          (!ascending && students[j].cgpa < key.cgpa))) {
            students[j + 1] = students[j];
            j--;
        }
        students[j + 1] = key;
    }
}

void displayStudents(Student* students, int size) {
    cout << "\nStudent Records:\n";
    for (int i = 0; i < size; i++)
        cout << "ID: " << students[i].id << ", Name: " << students[i].name
             << ", CGPA: " << students[i].cgpa << endl;
}

int main() {
    int capacity = 2, size = 0;
    Student* students = new Student[capacity];
    int choice;

    do {
        cout << "\n--- Student Database Menu ---\n";
        cout << "1. Add Student\n";
        cout << "2. Display Students\n";
        cout << "3. Sort by Name (Bubble Sort)\n";
        cout << "4. Sort by CGPA (Insertion Sort)\n";
        cout << "5. Search by ID (Binary Search)\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            addStudent(students, size, capacity);
            break;
        case 2:
            displayStudents(students, size);
            break;
        case 3:
            bubbleSortByName(students, size);
            cout << "Sorted by Name.\n";
            break;
        case 4: {
            int order;
            cout << "1. Ascending\n2. Descending\nChoose order: ";
            cin >> order;
            insertionSortByCGPA(students, size, order == 1);
            cout << "Sorted by CGPA.\n";
            break;
        }
        case 5: {
            int targetID;
            cout << "Enter ID to search: ";
            cin >> targetID;
            sort(students, students + size, [](Student a, Student b) { return a.id < b.id; });
            int index = binarySearch(students, size, targetID);
            if (index != -1)
                cout << "Found: " << students[index].name << ", CGPA: " << students[index].cgpa << endl;
            else
                cout << "Student not found.\n";
            break;
        }
        case 6:
            cout << "Exiting...\n";
            break;
        default:
            cout << "Invalid choice.\n";
        }
    } while (choice != 6);

    delete[] students;
    return 0;
}
✅ This code is clean, practical, and compatible with online compilers.
Let me know if you want a Python version, file saving, or performance timing added next.

