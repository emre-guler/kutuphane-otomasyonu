# Library Automation System

## Description
This project is a Library Automation System designed to manage library operations such as user registration, book management, and loan tracking. It provides a user-friendly interface for both administrators and users to interact with the library database. The system is built using Python and PyQt5 for the graphical user interface, with SQLite as the database backend.

## Features
- User Authentication
  - Admin login and registration
  - Secure password management
  - TC (Turkish Identity Number) verification
- Book Management
  - Add new books with details (name, author, page count)
  - Delete existing books
  - List all available books
  - Track book status (borrowed/available)
- User Management
  - Add new library members
  - Delete existing members
  - List all registered members
  - Track member activities
- Loan Management
  - Issue books to members
  - Track borrowed books
  - Handle book returns
  - View currently borrowed books
- Database Management
  - SQLite database for efficient data storage
  - Automatic database creation and table management
  - Data persistence across sessions

## Requirements
- Python 3.x
- PyQt5 (for GUI)
- SQLite3 (included in Python standard library)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/emre-guler/library-automation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd library-automation
   ```
3. Install the required packages:
   ```bash
   pip install PyQt5
   ```

## Usage
To run the application:
```bash
python index.py
```

The system will automatically create a `library.db` file on first run, which will store all the necessary data.

## Project Structure
- `index.py`: Main application file containing the GUI implementation
- `database.py`: Database operations and management
- `library.db`: SQLite database file (created automatically)

## Database Schema
The system uses four main tables:
- `adminAccount`: Stores administrator credentials
- `book`: Manages book information and status
- `userAccount`: Stores library member information
- `bookUser`: Tracks book loans and returns

## Contributing
Feel free to fork the project and submit pull requests for any improvements.