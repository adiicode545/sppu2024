class Library:
    def __init__(self):
        # Dictionary to store borrowing records {member_name: [list_of_books]}
        self.borrowing_records = {}
        # Dictionary to store book borrow counts {book_title: count}
        self.book_borrow_counts = {}

    def add_member(self, member_name):
        if member_name not in self.borrowing_records:
            self.borrowing_records[member_name] = []

    def borrow_book(self, member_name, book_title):
        if member_name not in self.borrowing_records:
            self.add_member(member_name)
        # Record the borrowing
        self.borrowing_records[member_name].append(book_title)
        # Update book borrow count
        if book_title not in self.book_borrow_counts:
            self.book_borrow_counts[book_title] = 0
        self.book_borrow_counts[book_title] += 1

    def compute_average_books(self):
        total_books = sum(len(books) for books in self.borrowing_records.values())
        total_members = len(self.borrowing_records)
        if total_members == 0:
            return 0
        return total_books / total_members

    def find_highest_and_lowest_borrowed_books(self):
        if not self.book_borrow_counts:
            return None, None
        highest = max(self.book_borrow_counts, key=self.book_borrow_counts.get)
        lowest = min(self.book_borrow_counts, key=self.book_borrow_counts.get)
        return highest, lowest

    def count_members_with_no_borrowings(self):
        return sum(1 for books in self.borrowing_records.values() if len(books) == 0)

    def most_frequently_borrowed_book(self):
        if not self.book_borrow_counts:
            return None
        # Mode → book(s) with maximum borrow count
        max_count = max(self.book_borrow_counts.values())
        most_frequent = [book for book, count in self.book_borrow_counts.items() if count == max_count]
        return most_frequent


# --------- Example Usage ---------
library = Library()

# Add members
library.add_member("Atharv")
library.add_member("Nilesh")
library.add_member("Kartik")

# Borrow books
library.borrow_book("Atharv", "Book A")
library.borrow_book("Atharv", "Book B")
library.borrow_book("Nilesh", "Book A")
library.borrow_book("Nilesh", "Book C")
library.borrow_book("Nilesh", "Book A")

# Compute average books borrowed
print("Average number of books borrowed:", library.compute_average_books())

# Find highest and lowest borrowed books
highest, lowest = library.find_highest_and_lowest_borrowed_books()
print("Most borrowed book:", highest)
print("Least borrowed book:", lowest)

# Count members with no borrowings
print("Members with no borrowings:", library.count_members_with_no_borrowings())

# Most frequently borrowed book(s)
print("Most frequently borrowed book(s):", library.most_frequently_borrowed_book())
