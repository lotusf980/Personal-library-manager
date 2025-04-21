import json
import os

LIBRARY_FILE = "library.txt"

# Load library from file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Display all books
def display_books(library):
    if not library:
        print("\nNo books in the library.\n")
        return
    for idx, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    print()

# Add a book
def add_book(library):
    title = input("Title: ")
    author = input("Author: ")
    try:
        year = int(input("Publication Year: "))
    except ValueError:
        print("Invalid year.")
        return
    genre = input("Genre: ")
    read_input = input("Have you read it? (yes/no): ").strip().lower()
    read = read_input == "yes"

    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    })
    print("Book added.\n")

# Remove a book
def remove_book(library):
    title = input("Enter the title to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("Book removed.\n")
            return
    print("Book not found.\n")

# Search books
def search_books(library):
    keyword = input("Search by title or author: ").strip().lower()
    results = [book for book in library if keyword in book["title"].lower() or keyword in book["author"].lower()]

    if results:
        for book in results:
            status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        print()
    else:
        print("No matching books found.\n")

# Show stats
def show_statistics(library):
    total = len(library)
    read_count = sum(book["read"] for book in library)
    percent = (read_count / total) * 100 if total > 0 else 0
    print(f"Total books: {total}")
    print(f"Books read: {read_count} ({percent:.2f}%)\n")

# Menu system
def main():
    library = load_library()

    while True:
        print("=== Personal Library Manager ===")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            show_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()