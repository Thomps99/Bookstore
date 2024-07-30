import json
import getpass

# Simulated Database
books = []
users = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "staff", "password": "staff123", "role": "staff"},
]
customers = []

def save_books():
    with open('books.json', 'w') as f:
        json.dump(books, f)

def load_books():
    global books
    try:
        with open('books.json', 'r') as f:
            books = json.load(f)
    except FileNotFoundError:
        books = []

def authenticate(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    price = float(input("Enter book price: "))
    books.append({"title": title, "author": author, "isbn": isbn, "price": price})
    save_books()
    print("Book added successfully.")

def remove_book():
    isbn = input("Enter ISBN of the book to remove: ")
    global books
    books = [book for book in books if book["isbn"] != isbn]
    save_books()
    print("Book removed successfully.")

def update_book():
    isbn = input("Enter ISBN of the book to update: ")
    for book in books:
        if book["isbn"] == isbn:
            book["title"] = input("Enter new title: ")
            book["author"] = input("Enter new author: ")
            book["price"] = float(input("Enter new price: "))
            save_books()
            print("Book updated successfully.")
            return
    print("Book not found.")

def search_books():
    query = input("Enter title or author to search: ")
    results = [book for book in books if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]
    if results:
        for book in results:
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Price: ${book['price']}")
    else:
        print("No books found.")

def view_books():
    if books:
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Price: ${book['price']}")
    else:
        print("No books available.")

def make_purchase():
    isbn = input("Enter ISBN of the book to purchase: ")
    for book in books:
        if book["isbn"] == isbn:
            print(f"You have purchased {book['title']} by {book['author']} for ${book['price']}.")
            return
    print("Book not found.")

def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Update Book")
        print("4. Search Books")
        print("5. View All Books")
        print("6. Log Out")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            update_book()
        elif choice == '4':
            search_books()
        elif choice == '5':
            view_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def staff_menu():
    while True:
        print("\nStaff Menu")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Search Books")
        print("4. View All Books")
        print("5. Log Out")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            search_books()
        elif choice == '4':
            view_books()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def customer_menu():
    while True:
        print("\nCustomer Menu")
        print("1. Search Books")
        print("2. View All Books")
        print("3. Make a Purchase")
        print("4. Log Out")
        choice = input("Enter your choice: ")
        if choice == '1':
            search_books()
        elif choice == '2':
            view_books()
        elif choice == '3':
            make_purchase()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    load_books()
    print("Welcome to the Online Bookstore Management System")
    while True:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        user = authenticate(username, password)
        if user:
            if user["role"] == "admin":
                admin_menu()
            elif user["role"] == "staff":
                staff_menu()
            
        else:
            print("Invalid credentials. Please try again.")
        another = input("Would you like to log in as another user? (y/n): ")
        if another.lower() != 'y':
            break

if __name__ == "__main__":
    main()
