#include <iostream>
#include <cstring>
using namespace std;

struct Student {
    int id;
    char name[50];
    float cgpa;
};

// 1. Add student with dynamic memory expansion
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

// 2. Linear Search by ID
int linearSearch(Student* students, int size, int targetID) {
    for (int i = 0; i < size; i++) {
        if (students[i].id == targetID)
            return i;
    }
    return -1;
}

// 3a. Selection Sort by Name
void selectionSortByName(Student* students, int size) {
    for (int i = 0; i < size - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < size; j++) {
            if (strcmp(students[j].name, students[minIdx].name) < 0)
                minIdx = j;
        }
        if (minIdx != i)
            swap(students[i], students[minIdx]);
    }
}

// 3b. Selection Sort by CGPA
void selectionSortByCGPA(Student* students, int size, bool ascending) {
    for (int i = 0; i < size - 1; i++) {
        int targetIdx = i;
        for (int j = i + 1; j < size; j++) {
            if ((ascending && students[j].cgpa < students[targetIdx].cgpa) ||
                (!ascending && students[j].cgpa > students[targetIdx].cgpa)) {
                targetIdx = j;
            }
        }
        if (targetIdx != i)
            swap(students[i], students[targetIdx]);
    }
}

// 4. Display all students
void displayStudents(Student* students, int size) {
    cout << "\nStudent Records:\n";
    for (int i = 0; i < size; i++) {
        cout << "ID: " << students[i].id
             << ", Name: " << students[i].name
             << ", CGPA: " << students[i].cgpa << endl;
    }
}

int main() {
    int capacity = 2, size = 0;
    Student* students = new Student[capacity];
    int choice;

    do {
        cout << "\n--- Student Database Menu ---\n";
        cout << "1. Add Student\n";
        cout << "2. Display Students\n";
        cout << "3. Sort by Name (Selection Sort)\n";
        cout << "4. Sort by CGPA (Selection Sort)\n";
        cout << "5. Search by ID (Linear Search)\n";
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
            selectionSortByName(students, size);
            cout << "Sorted by Name.\n";
            break;
        case 4: {
            int order;
            cout << "1. Ascending\n2. Descending\nChoose order: ";
            cin >> order;
            selectionSortByCGPA(students, size, order == 1);
            cout << "Sorted by CGPA.\n";
            break;
        }
        case 5: {
            int targetID;
            cout << "Enter ID to search: ";
            cin >> targetID;
            int index = linearSearch(students, size, targetID);
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
