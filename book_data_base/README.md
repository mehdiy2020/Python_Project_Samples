# 📚 BookDatabase: Python Book Collection Manager

A simple, in-memory Python class (`BookDatabase`) designed to manage a personal book collection. It uses a list of dictionaries as its backend and leverages the **`prettytable`** library to display the entire database in a clean, professional-looking Markdown table format suitable for command-line output.

## ✨ Features

* **Add** new book entries with comprehensive metadata.
* **View** individual book details using `pprint`.
* **View** the entire collection formatted as a beautiful, sortable table.
* **Update** existing book information selectively.
* **Delete** books from the database by title.

---

## 🛠️ Installation

This project requires Python 3.8+ and two external libraries: `prettytable` and `pprint` (which is standard).

### Prerequisites

You can install the required external library using `pip`:

```bash
pip install prettytable

Usage
Simply copy the BookDatabase class code into a Python file (e.g., book_manager.py) and instantiate the class in your main script.

📖 Class Structure Overview
The BookDatabase class manages the list of book records, stored in the self.booklist attribute. Each book is a dictionary with the following keys:

Key	Description	Type
Book Title	Primary identifier for the book.	str
Author(s)	List of authors.	list of str
Genre	The book's genre.	str
Translator(s)	List of translators (if applicable).	list of str
Publisher	Name of the publishing company.	str
Start Reading	Date the book was started (e.g., "YYYY-MM-DD").	str
Finish Reading	Date the book was finished.	str
Edition Number	Book edition (e.g., "1st Edition").	str
Published Year	Year of publication.	int

🚀 Methods and Examples
1. add_a_book_inf()
Adds a new book dictionary to the internal self.booklist.

Python

# Initialize the database
book_db = BookDatabase()

# Add a book with multiple authors
book_db.add_a_book_inf(
    "An Introduction to Statistical Learning",
    author_s=["Gareth James", "Daniel Witten", "Trevor Hastie", "Robert Tibshirani"],
    genre="Science - Data Science",
    start_date="2024-01-01",
    publisher="Springer",
    edition="2nd Edition",
    published_year=2020
)

# Add a book with a single author
book_db.add_a_book_inf(
    title = "FastAPI Modern Python Web Development",
    author_s="Bill Lubanovic", # Accepts a single string
    genre="Tech",
    published_year=2022
)
2. view_whole_database()
Prints the entire book collection as a markdown-formatted table, sorted by "Book Title" in descending order.


🤝 Contributing
Feel free to fork this project and add features like saving the database to a JSON file, filtering/searching capabilities, or adding a rating system!










