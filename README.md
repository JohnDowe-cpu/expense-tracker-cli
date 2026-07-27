# Expense Tracker CLI

A Python command-line application for tracking personal expenses, storing expense history, searching saved entries, and generating spending summaries.

Expense Tracker CLI allows users to log expenses, categorize purchases, calculate total money spent, and maintain a persistent expense history through a clean menu-driven interface. This project focuses on reusable code, input validation, file management, and maintainable program structure.

---

# Features

- Add expense entries
- Record expense date, category, amount, and notes
- Save expenses to persistent storage
- View all saved expenses
- Search expenses by keyword
- Calculate total expenses logged
- Calculate total money spent
- Format currency to two decimal places
- Validate required text fields
- Validate expense amount input
- Handle missing data files without crashing
- Menu-driven command-line interface

---

# Technologies Used

- Python 3
- File I/O
- Dictionaries
- Functions
- Loops
- Input Validation
- Exception Handling
- Type Hints
- Docstrings
- Constants
- UTF-8 File Encoding
- Git
- GitHub

---

# Project Structure

```
Expense-Tracker-CLI/
│
├── main.py
├── expenses.txt
└── README.md
```

---

# Skills Demonstrated

This project demonstrates:

- Modular application design
- Function decomposition
- Persistent file storage
- Reading and writing text files
- Parsing saved data
- Performing calculations from stored data
- Input validation
- Error handling with try/except
- Currency formatting
- String manipulation
- Program organization
- Version control using Git and GitHub

---

# Installation

Clone the repository:

```bash
git clone https://github.com/JohnDowe-cpu/expense-tracker-cli.git
```

Navigate into the project folder:

```bash
cd expense-tracker-cli
```

Run the application:

```bash
python main.py
```

---

# Menu

```text
Expense Tracker CLI

1. Add Expense
2. View Expenses
3. Search Expenses
4. View Spending Summary
5. Quit
```

---

# Example Spending Summary

```text
Spending Summary

Total expenses logged: 3
Total spent: $77.25
```

---

# Example Expense Entry

```text
Expense Log

Date: 2026-07-21
Category: Groceries
Amount: $24.50
Notes: Walmart run
```

---

# Learning Goals

This project was created to practice:

- Building larger Python command-line applications
- Organizing reusable helper functions
- Working with persistent data storage
- Validating user input
- Parsing saved file data
- Performing calculations from stored information
- Writing clean, maintainable Python code
- Applying Git for version control

---

# Future Improvements

Potential future enhancements include:

- Upgrade storage from text files to SQLite
- Edit existing expenses
- Delete expense entries
- Category-based spending summaries
- Monthly expense reports
- CSV export
- Improved search that displays full matching entries
- Expense filtering by date range
- User profiles
- Authentication

---

# Version History

- **v0.1** — Created menu system
- **v0.2** — Added expense logging
- **v0.3** — Added expense amount validation
- **v0.4** — Saved expenses to file
- **v0.5** — Added expense viewer
- **v0.6** — Added expense search
- **v0.7** — Added spending summary
- **v0.8** — Added required field validation
- **v0.9** — Formatted currency output
- **v1.0** — Initial public release
- **v1.1** — Added type hints
- **v1.2** — Replaced hard-coded filenames with constants
- **v1.3** — Added UTF-8 file encoding
- **v1.4** — Added function docstrings and completed code cleanup

---

# License

This project is intended for educational and portfolio purposes.
