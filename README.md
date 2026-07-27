# Expense Tracker CLI

Expense Tracker CLI is a Python command-line application for tracking personal expenses, saving them to a text file, searching saved expenses, and viewing a basic spending summary.

## Features

- Add expense entries
- Save expenses to a text file
- View saved expenses
- Search saved expenses
- View total expenses logged
- Calculate total money spent
- Validate required text fields
- Validate expense amount input
- Format money with two decimal places
- Handle missing data files without crashing

## Technologies Used

- Python
- Functions
- Dictionaries
- Loops
- File handling
- Input validation
- Exception handling
- String methods
- Type hints
- Docstrings
- Constants
- UTF-8 file encoding
- Git
- GitHub

## How to Run

Clone the repository or download the project files, then run:

```bash
python3 main.py
```

## Menu Options

```text
1. Add expense
2. View expenses
3. Search expenses
4. View spending summary
5. Quit
```

## Example Output

```text
Spending Summary
Total expenses logged: 3
Total spent: $77.25
```

## Sample Expense Entry

```text
Expense Log
Date: 2026-07-21
Category: Groceries
Amount: $24.50
Notes: Walmart run
--------------------
```

## What I Learned

This project helped me practice building a larger Python command-line application using reusable helper functions, persistent file storage, exception handling, input validation, string parsing, constants, type hints, and docstrings. It also strengthened my understanding of reading saved data from files and performing calculations to generate useful summaries.

## Version History

- v0.1: Created menu system
- v0.2: Added expense entry feature
- v0.3: Added expense amount validation
- v0.4: Saved expenses to file
- v0.5: Added saved expense viewer
- v0.6: Added expense search feature
- v0.7: Added spending summary
- v0.8: Added required field validation
- v0.9: Formatted expense amounts
- v1.0: Finalized first release
- v1.1: Added type hints throughout the project
- v1.2: Replaced hard-coded filenames with constants
- v1.3: Added UTF-8 encoding to file operations
- v1.4: Added function docstrings and completed code cleanup

## Future Improvements

- Upgrade storage from text files to SQLite
- Add update and delete features
- Add category-based spending summaries
- Add date format validation
- Add monthly spending reports
- Add CSV export