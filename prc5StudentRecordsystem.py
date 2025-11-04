class StudentNode:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None
        self.prev = None


class StudentRecordManagement:
    def __init__(self):
        self.head = None

    def add_student(self, roll, name, marks):
        new_node = StudentNode(roll, name, marks)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        print(f" Student {name} added successfully.")

    def delete_student(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                print(f"️ Student with Roll {roll} deleted.")
                return
            temp = temp.next
        print(" Student not found.")

    def update_student(self, roll, name=None, marks=None):
        temp = self.head
        while temp:
            if temp.roll == roll:
                if name:
                    temp.name = name
                if marks is not None:
                    temp.marks = marks
                print(f" Student with Roll {roll} updated.")
                return
            temp = temp.next
        print(" Student not found.")

    def search_student(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print(f"Found -> Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
                return temp
            temp = temp.next
        print(" Student not found.")
        return None
    def display(self):
        if not self.head:
            print(" No student records available.")
            return
        temp = self.head
        print("\n Student Records:")
        print("RollNo\tName\tMarks")
        while temp:
            print(f"{temp.roll}\t{temp.name}\t{temp.marks}")
            temp = temp.next

    def sort_records(self, key="roll", order="asc"):
        if not self.head or not self.head.next:
            return
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if key == "roll":
                    cond = (temp.roll > temp.next.roll)
                else:
                    cond = (temp.marks > temp.next.marks)

                if order == "desc":
                    cond = not cond

                if cond:
                    temp.roll, temp.next.roll = temp.next.roll, temp.roll
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next
        print(f" Records sorted by {key} ({order}).")

if __name__ == "__main__":
    system = StudentRecordManagement()

    system.add_student(1, "Nilesh", 85)
    system.add_student(3, "Anish", 75)
    system.add_student(2, "Atharv", 90)

    system.display()

    system.search_student(2)

    system.update_student(3, marks=80)

    system.delete_student(1)

    system.sort_records(key="marks", order="desc")
    system.display()
