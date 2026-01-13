## Python CLI Calculator

A command-line calculator built using Python that performs basic arithmetic operations and stores calculation history in a file.  
This project focuses on clean code structure, proper error handling, and automated testing.

---

## Features

- Supports basic arithmetic operations: `+`, `-`, `*`, `/`
- Command-based interface for better usability
- Stores calculation history persistently in a file
- Handles invalid input and edge cases gracefully
- Includes automated unit tests for core logic

---

## Commands

| Command | Description |
|--------|-------------|
| `history` | View saved calculation history |
| `clear` | Clear all saved history |
| `help` | Show available commands and usage |
| `exit` | Exit the calculator |

---

## Input Format

- number operator number

- Example Format: 5 * 6

---

## Project Structure

python-cli-calculator/
├── calculator.py
├── test_cases.py
├── history.txt
└── README.md


---

## How to Run the Calculator

1. Make sure Python is installed
2. Open terminal in the project directory
3. Run the following command:
    ├── python test_cases.py


---

## How to Run Tests

This project includes unit tests written using Python’s `unittest` module.

Run the tests using:
    ├── python test_cases.py


If all tests pass successfully, the output will show `OK`.

---

## What I Learned

- Writing modular and readable Python code
- Using file handling for persistent storage
- Implementing exception-based error handling
- Separating computation logic from input/output
- Writing basic unit tests to validate functionality

---

## Future Improvements

- We can add a web-based version using Django
- We can enhance history management features
- Support additional mathematical operations

---

## Author

Built as a learning project to strengthen Python fundamentals and basic software design practices.
